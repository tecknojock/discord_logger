import json
import logging
import os
import sys

class Config():
    def __init__(self):
        _logger = logging.getLogger()
        _json = None
        try:
            with open('config.json') as f:
                _json = json.load(f)
        except FileNotFoundError as e:
            _logger.critical('config.json not found. Aborting.')
            sys.exit(1)

        _logger.info('Parsing config.json')
        self.bot = bool(_json['bot'])
        self.db = str(_json['db'])
        self.token = str(_json['token'])

        self.sql = {}

        _logger.info('Parsing SQL')
        _sql_path = os.path.join(os.path.dirname(__file__), '_sql')

        with open(os.path.join(_sql_path, 'mkserverlist.sql')) as f:
            self.sql['mkserverlist'] = f.read()

        with open(os.path.join(_sql_path, 'mkserver.sql')) as f:
            self.sql['mkserver'] = f.read()

        with open(os.path.join(_sql_path, 'mkchannel.sql')) as f:
            self.sql['mkchannel'] = f.read()

        with open(os.path.join(_sql_path, 'inschannel.sql')) as f:
            self.sql['inschannel'] = f.read()

        with open(os.path.join(_sql_path, 'insserver.sql')) as f:
            self.sql['insserver'] = f.read()
