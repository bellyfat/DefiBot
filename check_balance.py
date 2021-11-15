import time
import logging
from web3 import Web3
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

    w3 = Web3(Web3.HTTPProvider(BSC))
    logging.info(w3.isConnected())

    spender = Web3.toChecksumAddress("0x7D57B8B8A731Cc1fc1E661842790e1864d5Cf4E8")

    erc20_abi = load_abi("erc20.json")

    while True:
        send_flag = False

        for addr, token in ((Tokens.HE, "HE"), (Tokens.NFTD, "NFTD"), (Tokens.YIN, "YIN")):
            contract = w3.eth.contract(address=addr, abi=erc20_abi)
            balance = contract.functions.balanceOf(spender).call()
            logging.info(f"{token} balance: {Web3.fromWei(balance, 'ether')}")
            if balance > 0:
                msg = f"{token} balance: {Web3.fromWei(balance, 'ether')}"
                send_telegram_notice(msg)
                send_flag = True

        if send_flag:
            time.sleep(60 * 60)
        else:
            time.sleep(60)



