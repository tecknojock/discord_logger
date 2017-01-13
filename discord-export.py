import argparse
import discord

client = discord.Client()
args = None


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('token',
                        help='token used for authenticating with Discord')

    parser.add_argument('path',
                        help='path to the root of the log database')

    parser.add_argument('-u', '-user-token',
                        help="token passed is a USER token, NOT a BOT token",
                        action="store_false")

    args = parser.parse_args()
    client.run()


@client.event
async def on_ready():
    print("logged in")


@client.event
async def on_message(message):
    print('[{}] {}: {}'
          .format(message.timestamp, message.author, message.content))

if __name__ == "__main__":
    main()
