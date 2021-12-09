import os
from web3 import Web3


BSC = "https://bsc-dataseed.binance.org/"
CELO = "https://forno.celo.org"
POLYGON = "https://rpc-mainnet.matic.quiknode.pro"

# Spender Address
SPENDER_ADDRESS = os.environ['spender_address']


class Tokens:
    HE = "0x20d39a5130f799b95b55a930e5b7ebc589ea9ed8"
    NFTD = "0xac83271abb4ec95386f08ad2b904a46c61777cef"
    BUSD = "0xe9e7cea3dedca5984780bafc599bd69add087d56"
    YIN = "0x794Baab6b878467F93EF17e2f2851ce04E3E34C8"
    NUM = "0xeceb87cf00dcbf2d4e2880223743ff087a995ad9"
    SOURCE = "0x74c0C58B99b68cF16A717279AC2d056A34ba2bFe"
    BEM = "0x5306be16e6af81140aa1cc4de45aa27f657f02b2"
    SIS = "0xd38bb40815d2b0c2d2c866e0c72c5728ffc76dd9"
    MGA = "0x03ac6ab6a9a91a0fcdec7d85b38bdfbb719ec02f"
    BLOCK = "0xbc7a566b85ef73f935e640a06b5a8b031cd975df"


for attr in dir(Tokens):
    if not attr.startswith('_'):
        setattr(Tokens, attr, Web3.toChecksumAddress(getattr(Tokens, attr)))

# telegram
TELEGRAM_CHAT_ID = "581220685"
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
