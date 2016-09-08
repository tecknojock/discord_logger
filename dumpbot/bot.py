import discord
import sqlite3
from config import Config

class DumpBot(discord.Client):
    def __init__(self):
        super().__init__()
        self.config = Config()
        self.conn = sqlite3.connect(self.config.db)
        self.cur = self.conn.cursor()
        self.cur.execute('''
                            CREATE TABLE IF NOT EXISTS servers (
                                TEXT PRIMARY KEY server_id,
                                TEXT name
                            );
                        ''')

    def run(self):
        print('Logging in...')
        super().run(self.config.token, bot=self.config.bot)

    async def on_message(self, message):
        print('Getting server list...')
        for s in discord.Client.servers:
            await dump_server(s)

    async def dump_server(self, id):
        #TODO: HOW DO
        #print('Dumping server id={}...'.format(discord.server))
        pass

    async def dump_channel(self, id):
        pass

if __name__ == '__main__':
    dumpbot = DumpBot()
    dumpbot.run()
