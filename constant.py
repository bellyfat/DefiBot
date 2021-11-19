import os
from web3 import Web3


BSC = "https://bsc-dataseed.binance.org/"


class Tokens:
    HE = "0x20d39a5130f799b95b55a930e5b7ebc589ea9ed8"
    NFTD = "0xac83271abb4ec95386f08ad2b904a46c61777cef"
    BUSD = "0xe9e7cea3dedca5984780bafc599bd69add087d56"
    YIN = "0x794Baab6b878467F93EF17e2f2851ce04E3E34C8"
    NUM = "0xeceb87cf00dcbf2d4e2880223743ff087a995ad9"


for attr in dir(Tokens):
    if not attr.startswith('_'):
        setattr(Tokens, attr, Web3.toChecksumAddress(getattr(Tokens, attr)))

# telegram
TELEGRAM_CHAT_ID = "581220685"
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
