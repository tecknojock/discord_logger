import argparse
import discord

client = discord.Client()


def main():
    parse_args()
    client.run(args.token, bot=(args.user if args.user is not None else True))


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('token',
                        help='token used for authenticating with Discord')

    parser.add_argument('path',
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
    print('[{}] {}: {}'
          .format(message.timestamp, message.author, message.content))


if __name__ == "__main__":
    main()
