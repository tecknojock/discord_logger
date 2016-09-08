import json
import os
import sys

class Config():
    def __init__(self):
        _json = None
        try:
            with open('config.json') as f:
                _json = json.load(f)
        except FileNotFoundError as e:
            print('config.json not found. Aborting.')
            sys.exit(1)
        self.bot = bool(_json['bot'])
        self.db = str(_json['db'])
        self.token = str(_json['token'])

        _sql_path = os.path.join(os.path.dirname(__file__), os.path.pardir, '_sql')
        # TODO: Add SQL files here!
        with open(os.path.join(_sql_path, 'mkserverlist.sql')) as f:
            pass

        with open(os.path.join(_sql_path, 'mkserver.sql')) as f:
            pass

        with open(os.path.join(_sql_path, 'mkchannel.sql')) as f:
            pass
