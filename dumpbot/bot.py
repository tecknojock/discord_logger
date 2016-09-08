import discord
import sqlite3
from config import Config

class DumpBot(discord.Client):
    def __init__(self):
        super().__init__()
        self.config = Config()
        self.conn = sqlite3.connect(self.config.db)
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS servers (
                                TEXT PRIMARY KEY server_id,
                                TEXT name
                            );''')

    def run(self):
        print('Logging in...')
        super().run(self.config.token, bot=self.config.bot)

    async def on_read(self, message):
        print('Getting server list...')
        for server in discord.Client.servers:
            await dump_server(server)

    async def dump_server(self, server):
        print('Dumping server id={}...'.format(server.id))
        self.cur.execute('''CREATE TABLE IF NOT EXISTS ? (
                                TEXT PRIMARY KEY channel_id,
                                TEXT name,
                                TEXT description
                        );''', server.id)
        for channel in server.channels:
            self.cur.execute('INSERT INTO ? VALUES (?, ?, ?);', \
                             server.id, channel.id, channel.name, channel.topic)
            await dump_channel(channel)

    async def dump_channel(self, channel):
        print('Dumping channel id={}...'.format(channel.id))
        pass

if __name__ == '__main__':
    dumpbot = DumpBot()
    dumpbot.run()
