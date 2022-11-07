class OperationException(Exception):
    def __init__(self):
        print("ERROR: ungültiges Operationszeichen eingegeben!")

class NumberFormatException(Exception):
    def __init__(self, value):
        super().__init__("ERROR:" + value + "ist ein ungültiger Zahlenwert")