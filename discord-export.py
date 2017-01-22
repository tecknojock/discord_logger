import argparse
import cfscrape
import discord
from hashlib import md5
import json
from mimetypes import guess_extension
import os

client = discord.Client()

# Yeah yeah, I know I use globals. You're not the first one to tell me. :P
global args
args = None
global blob_contexts
blob_contexts = []
global blobs
blobs = {}
global scraper
scraper = cfscrape.create_scraper()
global servers
servers = []


# Initialization Functions
def main():
    parse_args()
    client.run(args.token, bot=args.user)


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('token',
                        help='token used for authenticating with Discord')

    parser.add_argument('-p', '--path',
                        help='path to the root of the log database')

    parser.add_argument('-u', '--user',
                        help="token passed is a USER token, NOT a bot token",
                        action="store_false")

    global args
    args = parser.parse_args()


# Main Functions
@client.event
async def on_ready():
    await get_servers()
    await get_channels()


async def get_servers():
    global servers
    servers = read_json('servers.json')
    for server in client.servers:
        servers.append({
            'name': server.name,
            'region': str(server.region),
            'icon': server.icon,
            'id': server.id,
            'mfa_level': server.mfa_level,
            'verification_level': str(server.verification_level),
            'features': server.features,
            'splash': server.splash,
            'icon_url': download_blob(server.icon_url,
                                      server.icon)
            if server.icon_url is not '' else '',
            'splash_url': download_blob(server.splash_url,
                                        server.splash)
            if server.splash_url is not '' else '',
            'member_count': server.member_count,
            'created_at': server.created_at.isoformat()
        })

    servers = dedupe_list(servers)
    write_json('servers.json', servers)


async def get_channels():
    for server in client.servers:
        channels = read_json('{}/channels.json'.format(server.id))
        for channel in server.channels:
            channels.append({
                'name': channel.name,
                'id': channel.id,
                'topic': channel.topic,
                'position': channel.position,
                'type': str(channel.type),
                'bitrate': channel.bitrate,
                'user_limit': channel.user_limit,
                'is_default': channel.is_default,
                'mention': channel.mention,
                'created_at': channel.created_at.isoformat()
            })

        channels = dedupe_list(channels)
        write_json('{}/channels.json'.format(server.id), channels)


# Utility Functions
def read_json(path):
    path = os.path.join((args.path if args.path is not None else '.'), path)

    os.makedirs(os.path.split(path)[0], exist_ok=True)

    try:
        with open(path, 'rt') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def write_json(path, obj):
    path = os.path.join((args.path if args.path is not None else '.'), path)

    os.makedirs(os.path.split(path)[0], exist_ok=True)

    with open(path, 'wt') as f:
        json.dump(obj, f, indent=4, separators=(', ', ': '), sort_keys=True)


def dedupe_list(lst):
    ids = []
    deduped_lst = []
    for i in lst:
        if i['id'] not in ids:
            deduped_lst.append(i)
            ids.append(i['id'])
    return deduped_lst


def download_blob(url, cksum, ctx=''):
    path = os.path.join((args.path if args.path is not None else '.'),
                        ctx, 'blobs')

    os.makedirs(path, exist_ok=True)

    global blob_contexts
    global blobs
    if ctx not in blob_contexts:
        blob_contexts.append(ctx)
        for b in os.listdir(path):
            b = b.split('.')
            blobs[b[0]] = (b[1], ctx)

    if cksum in blobs:
        return os.path.join(ctx, 'blobs', cksum + '.' + blobs[cksum][0])

    blob = scraper.get(url)
    hash = md5(blob.content).hexdigest()
    ext = guess_extension(blob.headers['content-type'])
    name = hash + ext

    with open(os.path.join(path, name), 'wb') as f:
        f.write(blob.content)

    blobs[hash] = (ext.split('.')[1], ctx)

    return os.path.join(ctx, 'blobs', name)


if __name__ == "__main__":
    main()
