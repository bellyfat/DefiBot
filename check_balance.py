import time
import logging
from web3 import Web3
from web3.auto.infura import w3
from utils import load_abi
from constant import BSC, CELO, POLYGON, Tokens, SPENDER_ADDRESS
from utils import send_telegram_notice
from log_config import config_logging


if __name__ == '__main__':
    config_logging()

    bsc_w3 = Web3(Web3.HTTPProvider(BSC))
    celo_w3 = Web3(Web3.HTTPProvider(CELO))
    polygon_w3 = Web3(Web3.HTTPProvider(POLYGON))
    logging.info(f"bsc: {bsc_w3.isConnected()}")
    logging.info(f"celo: {celo_w3.isConnected()}")
    logging.info(f"polygon: {polygon_w3.isConnected()}")
    logging.info(f"eth: {w3.isConnected()}")

    spender = Web3.toChecksumAddress(SPENDER_ADDRESS)

    erc20_abi = load_abi("erc20.json")
    check_list = (
        (Tokens.HE, "HE", "bsc"),
        (Tokens.NFTD, "NFTD", "bsc"),
        (Tokens.YIN, "YIN", "eth"),
        (Tokens.NUM, "NUM", "bsc"),
        (Tokens.SOURCE, "SOURCE", "celo"),
        (Tokens.BEM, "BEM", "bsc"),
        (Tokens.SIS, "SIS", "eth"),
        (Tokens.MGA, "MGA", "bsc"),
        (Tokens.BLOCK, "BLOCK", "bsc"),
        (Tokens.ONE_SOL, "1SOL", "eth"),
        (Tokens.MSU, "MSU", "polygon"),
        (Tokens.MGOD, "MGOD", "bsc"),
        (Tokens.WAM, "WAM", "bsc"),
        (Tokens.SRG, "SRG", "bsc"),
    )

    while True:
        send_flag = False

        for addr, token, network in check_list:
            kwargs = {"address": addr, "abi": erc20_abi}
            if network == "bsc":
                contract = bsc_w3.eth.contract(**kwargs)
            elif network == "celo":
                contract = celo_w3.eth.contract(**kwargs)
            elif network == "polygon":
                contract = polygon_w3.eth.contract(**kwargs)
            else:
                contract = w3.eth.contract(**kwargs)
            balance = contract.functions.balanceOf(spender).call()
            logging.info(f"{token} balance({network}): {Web3.fromWei(balance, 'ether')}")
            if balance > 0:
                msg = f"{token} balance({network}): {Web3.fromWei(balance, 'ether')}"
                send_telegram_notice(msg)
                send_flag = True

        if send_flag:
            time.sleep(60 * 60)
        else:
            time.sleep(30)



