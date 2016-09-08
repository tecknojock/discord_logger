import discord
import sqlite3

class DumpBot(discord.Client):
    def __init__(self):
        super().__init__()
        self.config = Config()
        self.conn = sqlite3.connect(self.config.db)

    def run():
        super().run(self.config.token, bot=self.config.bot)

    async def on_message(self, message):
        pass

if __name__ == '__main__':
    dumpbot = DumpBot()
    dumpbot.run()