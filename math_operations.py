from abc import ABC, abstractmethod


class MathOp(ABC):
    """
    Eine abstrakte Klasse, die eine beliebige mathematische Operation repräsentiert.
    Die Methode execute_op wird abstrakt implementiert und muss durch konkrete Klassen überschrieben werden.
    Die Methode result liefert das Ergebnis der ausgeführten Operation.
    """

    def __init__(self):
        """
        Initialisiert den Ergebniswert.
        Dieser wird auch in den abgeleiteten Klassen benötigt, so dass er hier als protected deklariert werden muss.
        """
        self._result = 0.0
    # ergänzen Sie hier die abstrakte Methode execute_op. Sie erhält zwei Parameter. Diese werden dann in
    # den abgeleiteten Klassen je nach Operation verrechnet.
    @abstractmethod
    def execute_op(self, val1, val2):
        pass

    # erstellen Sie hier ein Property, das den Wert der Berechnung (ein Attribut, das Sie definieren müssen)
    # zurückgibt
    @property
    def result(self):
        return self._result


class Adder(MathOp):
    """
    Addiert zwei Zahlen.
    """
    # Implementieren Sie hier die Methode execute_op in der konkreten Umsetzung für einen Addierer.
    def execute_op(self, val1, val2):
        self._result = val1 + val2


# Implementieren Sie hier die Klasse Subtractor
class Subtractor(MathOp):
    """
    Subtrahiert zwei Zahlen.
    """
    def execute_op(self, val1, val2):
        self._result = val1 - val2


# Implementieren Sie hier die Klasse Multiplier
class Multiplier(MathOp):
    """
    Multipliziert zwei Zahlen.
    """
    def execute_op(self, val1, val2):
        self._result = val1 * val2


# Implementieren Sie hier die Klasse Divider
class Divider(MathOp):
    """
    Dividiert zwei Zahlen.
    """
    def execute_op(self, val1, val2):
        """
        if val2 == 0:
            raise ZeroDivisionError(print("ERROR: Division durch Null ist nicht erlaubt!"))
        else:
            self._result = val1 / val2
        """
        self._result = val1 / val2

class Exponentiation(MathOp):
    """
    Exponiert zwei Zahlen.
    """
    def execute_op(self, val1, val2):
        self._result = val1 ** val2

class Rooter(MathOp):
    """
    Wurzel ziehen
    """
    def execute_op(self, val1, val2):
        self._result = val1 ** (1/val2)

class Faculity(MathOp):
    """
    Fakultät
    """
    def execute_op(self, val1, val2):
        for i in range(1, int(val1)):
            self._result = val1 * (val1 - 1)
            if val1 == 0:
                break


# Beachten Sie bitte, dass der Divisor nicht 0 sein darf. In diesem Fall soll die Methode
# einen ZeroDivisionError werfen.
