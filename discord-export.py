import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print("logged in")


@client.event
async def on_message(message):
    print('[{}] {}: {}'
          .format(message.timestamp, message.author, message.content))

if __name__ == "__main__":
    client.run(os.environ['EXPORT_TOKEN'], bot=False)
