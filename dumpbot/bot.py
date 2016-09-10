import logging
import discord
import sqlite3
import sys

from config import Config

logging.basicConfig(level=logging.INFO)

class DumpBot(discord.Client):
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger()
        self.config = Config()
        self.conn = sqlite3.connect(self.config.db, isolation_level='IMMEDIATE')
        self.conn.execute(self.config.sql['mkserverlist'])

    def run(self):
        super().run(self.config.token, bot=self.config.bot)

    async def on_ready(self):
        for server in self.servers:
            self.conn.execute(self.config.sql['insserver'], \
                              (server.id, server.name))
            await self.dump_server(server)
        sys.exit(0)

    async def dump_server(self, server):
        self.logger.info('Dumping server id=%s', server.id)
        self.conn.execute(self.config.sql['mkserver'].format(server.id))
        for channel in server.channels:
            self.conn.execute(self.config.sql['inschannel'].format(server.id), \
                             (channel.id, channel.name, channel.topic))
            await self.dump_channel(channel)

    async def dump_channel(self, channel):
        self.logger.info('Dumping channel id=%s', channel.id)
        self.logger.warn('Channel dumping not implemented yet')

if __name__ == '__main__':
    dumpbot = DumpBot()
    dumpbot.run()
