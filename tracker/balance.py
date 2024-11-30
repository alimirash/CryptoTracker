import requests

API_KEY = "5N61AGZW1CKDCD94N16CVK5CTQWIC7JQGD"

wallets = [
    "0x00000000219ab540356cBB839Cbe05303d7705Fa",
    "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
    "0xBE0eB53F46cd790Cd13851d5EFf43D12404d33E8",
    "0x40B38765696e3d5d8d9d834D8AaD4bB6e418E489",
    "0x8315177aB297bA92A06054cE80a67Ed4DBd7ed3a",
    "0x49048044D57e1C92A77f79988d21Fa8fAF74E97e",
    "0xDA9dfA130Df4dE4673b89022EE50ff26f6EA73Cf",
    "0x47ac0Fb4F2D84898e4D9E7b4DaB3C24507a6D503",
    "0xF977814e90dA44bFA03b6295A0616a897441aceC",
    "0x742d35Cc6634C0532925a3b844Bc454e4438f44e",
    "0xa6715EAFe5D215B82cb9e90A9d6c8970A7C90033",
    "0xbEb5Fc579115071764c7423A4f12eDde41f106Ed",
    "0xC61b9BB3A7a0767E3179713f3A5c7a9aeDCE193C",
    "0xE92d1A43df510F82C66382592a047d288f85226f",
    "0x1Db92e2EeBC8E0c075a02BeA49a2935BcD2dFCF4",
    "0x0E58e8993100F1CBe45376c410F97f4893d9BfCD",
    "0x61EDCDf5bb737ADffE5043706e7C5bb1f1a56eEA",
    "0x28C6c06298d514Db089934071355E5743bf21d60",
    "0xcA8Fa8f0b631EcdB18Cda619C4Fc9d197c8aFfCa",
    "0x3BfC20f0B9aFcAcE800D73D2191166FF16540258",
    "0x866c9a77d8Ab71d2874703e80cb7aD809b301e8e",
    "0x8103683202aa8DA10536036EDef04CDd865C225E",
    "0xD3a22590f8243f8E83Ac230D1842C9Af0404C4A1",
    "0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe",
    "0x8696e84aB5e78983f2456bCB5c199eEa9648C8C2",
    "0x0a4c79cE84202b03e95B7a692E5D728d83C44c76",
    "0x2B6eD29A95753C3Ad948348e3e7b1A251080Ffb9",
    "0x539C92186f7C6CC4CbF443F26eF84C595baBBcA1",
    "0x868daB0b8E21EC0a48b726A1ccf25826c78C6d7F",
    "0xbFbBFacCD1126A11b8F84C60b09859F80f3BD10F"
]

def one_balance(wallet):
    url = f"https://api.etherscan.io/api"
    params = {
        "module": "account",
        "action": "balance",
        "address": wallet,
        "tag": "latest",
        "apikey": API_KEY,
    }
    response = requests.get(url, params=params)
    data = response.json()
    if data["status"] == "1":
        return int(data["result"])
    else:
        print(f"Error fetching balance for {wallet}: {data['message']}")
        return 0

def all_wallets_balance():
    wallet_balances = []
    for wallet in wallets:
        balance = one_balance(wallet)
        wallet_balances.append((wallet, balance))

    top_wallets = sorted(wallet_balances, key=lambda x: x[1], reverse=True)[:30]

    print("Top 30 Wallets by ETH Balance:")
    human_readble = unpack(wallets=top_wallets)
    print(human_readble)

def unpack(wallets):
    human_readble_wei_to_eth = []
    for rank, (wallet, balance) in enumerate(balance, start=1):
        human_readble_wei_to_eth.append(rank, wallet, balance / 1e18)

all_wallets_balance()
