import logging
import discord
import sqlite3
from config import Config

logging.basicConfig(level=logging.INFO)

class DumpBot(discord.Client):
    def __init__(self):
        super().__init__()
        self.config = Config()
        self.conn = sqlite3.connect(self.config.db)
        self.cur = self.conn.cursor()
        self.cur.execute(self.config.sql['mkserverlist'])

    def run(self):
        super().run(self.config.token, bot=self.config.bot)

    async def on_read(self, message):
        for server in discord.Client.servers:
            await dump_server(server)

    async def dump_server(self, server):
        print('Dumping server id={}...'.format(server.id))
        self.cur.execute(self.config.sql['mkserver'], server.id)
        for channel in server.channels:
            self.cur.execute(self.config.sql['inschannel'], \
                             server.id, channel.id, channel.name, channel.topic)
            await dump_channel(channel)

    async def dump_channel(self, channel):
        print('Dumping channel id={}...'.format(channel.id))
        pass

if __name__ == '__main__':
    dumpbot = DumpBot()
    dumpbot.run()
