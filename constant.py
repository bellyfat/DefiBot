import os
from web3 import Web3


BSC = "https://bsc-dataseed.binance.org/"
CELO = "https://forno.celo.org"
POLYGON = "https://rpc-mainnet.matic.quiknode.pro"
BOBA = "https://mainnet.boba.network/"

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
    ONE_SOL = "0x009178997aff09a67d4caccfeb897fb79d036214"
    MSU = "0xe8377a076adabb3f9838afb77bee96eac101ffb1"
    MGOD = "0x10A12969cB08a8d88D4BFB5d1FA317d41e0fdab3"
    WAM = "0xebbaeff6217d22e7744394061d874015709b8141"
    SRG = "0x722f41f6511ff7cda73a1cb0a9ea2f731738c4a0"
    SYN = "0xb554a55358ff0382fb21f0a478c3546d1106be8c"
    F2C = "0x657b632714e08ac66b79444ad3f3875526ee6689"
    MGG = "0x6125adcab2f171bc70cfe2caecfec5509273a86a"
    ISKY = "0x5DFD5edFde4d8EC9e632dCA9d09Fc7E833f74210"
    BBS = ""
    SPELL_ETH = "0x3A0b022f32b3191D44E5847da12dc0B63fb07C91"
    SPELL_BSC = "0xd6F28f15A5CaFc8d29556393c08177124B88de0D"


for attr in dir(Tokens):
    if attr and not attr.startswith('_'):
        try:
            setattr(Tokens, attr, Web3.toChecksumAddress(getattr(Tokens, attr)))
        except ValueError:
            pass

# telegram
TELEGRAM_CHAT_ID = "581220685"
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
