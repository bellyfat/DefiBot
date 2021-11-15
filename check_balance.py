import time
import logging
from web3 import Web3
from web3.auto.infura import w3
from utils import load_abi
from constant import BSC, Tokens
from utils import send_telegram_notice


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s.%(msecs)03d (%(levelname)s): %(message)s",
        datefmt="%y-%m-%d %H:%M:%S"
    )

    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger()

    bsc_w3 = Web3(Web3.HTTPProvider(BSC))
    logging.info(f"bsc: {bsc_w3.isConnected()}")
    logging.info(f"eth: {w3.isConnected()}")

    spender = Web3.toChecksumAddress("0x7D57B8B8A731Cc1fc1E661842790e1864d5Cf4E8")

    erc20_abi = load_abi("erc20.json")
    check_list = (
        (Tokens.HE, "HE", "bsc"),
        (Tokens.NFTD, "NFTD", "bsc"),
        (Tokens.YIN, "YIN", "eth")
    )

    while True:
        send_flag = False

        for addr, token, network in check_list:
            kwargs = {"address": addr, "abi": erc20_abi}
            if network == "bsc":
                contract = bsc_w3.eth.contract(**kwargs)
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
            time.sleep(60)



