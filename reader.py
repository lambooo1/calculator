class Reader:
    """
    Die Klasse dient dem Einlesen einer Eingabe. Sie ist als Singleton ausgelegt, da die
    Eingabe (Tastatur) ein Device darstellt, das physisch einmal vorhanden ist.
    """
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Reader, cls).__new__(cls)
        return cls.instance

    def scree_info(self):
        print("Geben Sie eine Rechnung in der Form 5 + 7 ein. \nFühren Sie die Berechnung mit <ENTER> aus.")

    def read(self):
        return input("Eingabe: ")


# TEST
if __name__ == "__main__":
    reader = Reader()
    reader.scree_info()
    value = reader.read()
    print(value)