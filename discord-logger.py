import discord
from os import environ

client = discord.Client()


def _main(token):
    pass


if __name__ == '__main__':
    _main(environ['DISCORD_TOKEN'])
