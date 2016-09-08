import json
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
