import MetaTrader5 as mt5
import pandas as pd
from config import account, password, server

def initialize_mt5():
    if not mt5.initialize():
        print("Initialize() failed")
        mt5.shutdown()
        return False
    if not mt5.login(account, password=password, server=server):
        print("Login failed")
        mt5.shutdown()
        return False
    return True

def send_order(symbol, order_type):
    tick = mt5.symbol_info_tick(symbol)
    price = tick.ask if order_type == mt5.ORDER_TYPE_BUY else tick.bid
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": 0.01,
        "type": order_type,
        "price": price,
        "deviation": 10,
        "comment": "python script open",
        "type_time": mt5.ORDER_TIME_GTC,
        "magic": 234000,
    }
    return mt5.order_send(request)

def main():
    if not initialize_mt5():
        return
    df = pd.read_csv('symbols.csv')
    for index, row in df.iterrows():
        symbol = row['Symbol']
        action = row['Action']
        if action == 'Buy':
            order_type = mt5.ORDER_TYPE_BUY
        elif action == 'Sell':
            order_type == mt5.ORDER_TYPE_SELL
        else:
            continue  # Skip if action is 'None'
        result = send_order(symbol, order_type)

if __name__ == "__main__":
    main()
