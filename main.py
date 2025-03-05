from Trader.config import account, password, server
from Tracker import trade
from Analyser.analyser import Analyser

def main():

    analyser = Analyser()
    signal = analyser.detect_signals()
    trade.main()

if __name__ == "__main__":
    main()