import discord

client = discord.Client()


def _main(token):
    if token is None:
        raise EnvironmentError(
            "DISCORD_TOKEN is undefined. Did you forget to set it?")
