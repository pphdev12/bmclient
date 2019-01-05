# pylint:disable=missing-docstring

"""

GITHUB: https://github.com/BitMEX/api-connectors
API: https://www.bitmex.com/app/wsAPI
TESTNET API: https://testnet.bitmex.com/app/wsAPI
"""


import json
import logging
import logging.handlers

import tornado.ioloop
from bitmex_websocket import BitMEXWebsocket


__CONTEXT_FILE__ = 'testnet.json'
with open(__CONTEXT_FILE__) as rf:
  __CONTEXT__ = json.load(rf)

LOG_FORMAT = '%(levelname)s\t%(created)f\t'\
             '%(lineno)d\t%(module)s\t'\
             '%(funcName)s\t%(message)s'


def _init_logger():
  logger = logging.getLogger()
  logger.level = logging.DEBUG
  handler = logging.StreamHandler()
  handler.setFormatter(logging.Formatter(LOG_FORMAT))
  logger.addHandler(handler)

  max_bytes = 10485760   # 10MB
  backup_count = 5
  handler = logging.handlers.RotatingFileHandler('bm.log',
                                                 maxBytes=max_bytes,
                                                 backupCount=backup_count)
  handler.setFormatter(logging.Formatter(LOG_FORMAT))
  logger.addHandler(handler)


def run():
  logging.info("Connecting... %s", __CONTEXT__['endpoint'])
  _client = BitMEXWebsocket(endpoint=__CONTEXT__['endpoint'],
                            symbol=__CONTEXT__['symbol'],
                            api_key=__CONTEXT__['api_key'],
                            api_secret=__CONTEXT__['api_secret'])
  logging.info("connected.")
  """
  _ret = _client.get_instrument()
  logging.info("INS: %s", _ret)
  _ret = _client.get_ticker()
  logging.info("TIC: %s", _ret)
  _ret = _client.market_depth()
  logging.info("DEP: %s", _ret)
  #print(_client.data)
  #_client.open_orders()
  _ret = _client.recent_trades()
  logging.info("RET: %s", _ret)
  """

  _ret = _client.funds()
  logging.info("FUN: %s", _ret)

  logging.info(dir(_client.ws))

if __name__ == '''__main__''':
  _init_logger()
  _loop = tornado.ioloop.IOLoop.current()
  print(dir(_loop))
  _loop.add_callback(run)
  _loop.start()
