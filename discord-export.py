import argparse
import discord
import os
import json

client = discord.Client()


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

    global args  # Yeah yeah, I used a global. Sue me, I don't care. P:
    args = parser.parse_args()


@client.event
async def on_ready():
    print("logged in")


@client.event
async def on_message(message):
    pass


async def get_servers():
    pass


def read_json(path):
    try:
        with open(os.path.join((args.path if args.path is not None else '.'),
                  path), 'rt') as f:
            return json.load(f)
    except FileNotFoundError:
        return ()


def write_json(path, obj):
    with open(os.path.join((args.path if args.path is not None else '.'),
              path), 'wt') as f:
        json.dump(f, indent=4, separators=(', ', ': '))


if __name__ == "__main__":
    main()
