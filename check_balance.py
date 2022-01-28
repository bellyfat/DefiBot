import time
import logging
from web3 import Web3
from web3.auto.infura import w3
from solana.rpc.api import Client
from utils import load_abi
from constant import BSC, CELO, POLYGON, Tokens, SPENDER_ADDRESS
from utils import send_telegram_notice
from log_config import config_logging


if __name__ == '__main__':
    config_logging()

    bsc_w3 = Web3(Web3.HTTPProvider(BSC))
    celo_w3 = Web3(Web3.HTTPProvider(CELO))
    polygon_w3 = Web3(Web3.HTTPProvider(POLYGON))
    solana_client = Client('https://api.mainnet-beta.solana.com')
    logging.info(f"bsc: {bsc_w3.isConnected()}")
    logging.info(f"celo: {celo_w3.isConnected()}")
    logging.info(f"polygon: {polygon_w3.isConnected()}")
    logging.info(f"eth: {w3.isConnected()}")
    logging.info(f"solana: {solana_client.is_connected()}")

    spender = Web3.toChecksumAddress(SPENDER_ADDRESS)

    erc20_abi = load_abi("erc20.json")
    check_list = (
        (Tokens.HE, "HE", "bsc", "cost: 0.01"),
        (Tokens.NFTD, "NFTD", "bsc", "cost: 0.1"),
        (Tokens.YIN, "YIN", "eth", "cost: 0.3"),
        (Tokens.NUM, "NUM", "bsc", "cost: 0.04"),
        (Tokens.SOURCE, "SOURCE", "celo", "cost: 0.45"),
        (Tokens.BEM, "BEM", "bsc", "cost: 0.01"),
        (Tokens.SIS, "SIS", "eth", "cost: 0.8"),
        (Tokens.MGA, "MGA", "bsc", "cost: 0.7"),
        (Tokens.ONE_SOL, "1SOL", "eth", "cost: 0.38"),
        (Tokens.MSU, "MSU", "polygon", "cost: 0.03"),
        (Tokens.MGOD, "MGOD", "bsc", "cost: 0.045"),
        (Tokens.WAM, "WAM", "bsc", "cost: 0.02"),
        (Tokens.SRG, "SRG", "bsc", "cost: 0.08"),
        (Tokens.F2C, "F2C", "bsc", "cost: 0.022"),
        (Tokens.MGG, "MGG", "bsc", "cost: 0.08"),
        (Tokens.ISKY, "ISKY", "polygon", "cost: 0.22"),
        # (Tokens.BBS, "BBS", "eth", "cost: 0.04"),
        (Tokens.SPELL_BSC, "SPELL", "bsc", "cost: 0.025"),
        (Tokens.SPELL_ETH, "SPELL", "eth", "cost: 0.025"),
        (Tokens.CWAR, "CWAR", "solana", "cost: 0.028"),
        (Tokens.BLOCK, "BLOCK", "solana", "cost: 0.078"),
        (Tokens.UNQ, "UNQ", "solana", ""),
        (Tokens.MEAN, "MEAN", "solana", ""),
        (Tokens.GWT, "GWT", "solana", ""),
        (Tokens.SLC, "SLC", "solana", "cost: 0.07"),
        (Tokens.SVT, "SVT", "solana", "cost: 0.3"),
        (Tokens.NOS, "NOS", "solana", "cost: 0.1"),
        (Tokens.CMFI, "CMFI", "solana", "cost: 0.08"),
        (Tokens.HBB, "HBB", "solana", "cost: 1"),
    )

    while True:
        send_flag = False

        for addr, token, network, remark in check_list:
            if network == "solana":
                rst = solana_client.get_token_account_balance(addr)
                balance = int(rst['result']['value']['amount'])
                balance_of_readable = rst['result']['value']['uiAmountString']
            else:
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
                balance_of_readable = Web3.fromWei(balance, 'ether')

            logging.info(f"{token} balance({network}): {balance_of_readable}")
            if balance > 0:
                msg = f"{token} balance({network}): {balance_of_readable} [{remark}]"
                send_telegram_notice(msg)
                send_flag = True

        if send_flag:
            time.sleep(60 * 60)
        else:
            time.sleep(30)



