import logging
import discord
import sqlite3
from config import Config

logging.basicConfig(level=logging.INFO)

class DumpBot(discord.Client):
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger()
        self.config = Config()
        self.conn = sqlite3.connect(self.config.db)
        self.cur = self.conn.cursor()
        #self.cur.execute(self.config.sql['mkserverlist'])

    def run(self):
        super().run(self.config.token, bot=self.config.bot)

    async def on_ready(self):
        for server in self.servers:
            await self.dump_server(server)

    async def dump_server(self, server):
        self.logger.info('Dumping server id=%s', server.id)
        #self.cur.execute(self.config.sql['mkserver'], server.id)
        for channel in server.channels:
            #self.cur.execute(self.config.sql['inschannel'], \
                             #server.id, channel.id, channel.name, channel.topic)
            await self.dump_channel(channel)

    async def dump_channel(self, channel):
        self.logger.info('Dumping channel id=%s', channel.id)
        pass

if __name__ == '__main__':
    dumpbot = DumpBot()
    dumpbot.run()
