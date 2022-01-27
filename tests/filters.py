import logging
import time
from web3 import Web3
from constant import BSC
from log_config import config_logging


if __name__ == '__main__':
    config_logging()

    w3 = Web3(Web3.HTTPProvider(BSC))
    new_block_filter = w3.eth.filter('latest')
    while True:
        new_enter = new_block_filter.get_new_entries()
        if new_enter:
            logging.info(w3.eth.block_number)
        time.sleep(1)

