import discord
import logging
import sqlite3
import sys

from config import Config
from hashlib import sha512

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
        self.conn.execute(self.config.sql['mkchannel'].format(channel.id))
        async for message in client.logs_from(channel):
            _names = [a.filename for a in message.attachments]
            # TODO: Download files, dump to FS, and get *actual* SHA-512 hashes
            _hashes = [a.id for a in message.attachments]
            self.conn.execute(self.config.sql['insmesg'].format(channel.id), \
                             (message.id, message.timestamp.isoformat(), message.author, \
                              message.content, str(_names), str(_hashes)))
        self.logger.info('Dump done for channel id=%s', channel.id)

if __name__ == '__main__':
    dumpbot = DumpBot()
    dumpbot.run()
