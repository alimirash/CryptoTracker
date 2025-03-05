from wallet_types import States

class Analyser:
    """
    Analyser:
        This class handles the analysis of active wallets retrieved from the Tracker
        by evaluating various metrics and transaction patterns.
    """
    def __init__(self , source_type, destination_type , amount):
        pass

    def analyse_wallet_transfer(self):
        if self.source_type == States.EXCHANGE and self.destination_type == States.PERSONAL:
            return "Buy"
        elif self.source_type == States.PERSONAL and self.destination_type == States.EXCHANGE:
            return "Sell"
        return 0

    def detect_signals(self):
        result = self.analyse_wallet_transfer()
        return result


