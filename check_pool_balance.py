import logging
import time

from web3 import Web3
from constant import BOBA, Tokens
from utils import send_telegram_notice, load_abi
from log_config import config_logging


if __name__ == '__main__':
    config_logging()
    boba_w3 = Web3(Web3.HTTPProvider(BOBA))
    logging.info(f"boba: {boba_w3.isConnected()}")

    erc20_abi = load_abi("erc20.json")

    check_list = (
        (Tokens.SYN, "SYN", "boba", "0xd5609cD0e1675331E4Fb1d43207C8d9D83AAb17C", 120),
    )

    while True:
        send_flag = False

        for addr, token, network, pool_addr, min_balance in check_list:
            kwargs = {"address": addr, "abi": erc20_abi}
            if network == "boba":
                contract = boba_w3.eth.contract(**kwargs)
            else:
                raise Exception("unsupported network")

            balance = Web3.fromWei(contract.functions.balanceOf(pool_addr).call(), 'ether')
            logging.info(f"{token} balance({network}): {balance}")
            if balance > min_balance:
                msg = f"{token} balance({network}): {balance}"
                send_telegram_notice(msg)
                send_flag = True

            if send_flag:
                time.sleep(60 * 60)
            else:
                time.sleep(30)
