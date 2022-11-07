from reader          import Reader
from math_operations import *
from tokenizer       import Tokenizer
from exceptions      import OperationException, NumberFormatException
'''
Hauptprogramm des Rechners.
'''

class Calculator:

    @staticmethod
    def main():
        """
        Hauptprogramm des Rechners.
        """
        z = True
        while z == True:
                # eine Referenz für das spätere Mathematik-Objekt bereitstellen.
                mathop = None
                # die Grundklassen instanziieren
                reader = Reader()
                tokenizer = Tokenizer()
                # Eingabe für eine Rechnung realisieren....
                reader.scree_info()
                value = reader.read()
                #print(value)
                tokenizer.add_operation("^")
                tokenizer.add_operation("r")
                tokenizer.add_operation("!")
                # Hier die möglichen Fehlerfälle, die beim Tokenizer anfallen können, abfangen.
                try:
                    tokenizer.split(value)


                # Jetzt wird's spannend!
                # splitten Sie die Eingabe mittels Tokenizer-Objekt auf.
                # Anhand der Operation entscheiden Sie nun, welche Klasse für mathop zu instanzieren ist.
                # Das machen Sie in einer if-elif-Kette.
                    if tokenizer.operation == "+":
                        mathop = Adder()
                    elif tokenizer.operation == "-":
                        mathop = Subtractor()
                    elif tokenizer.operation == "*":
                        mathop = Multiplier()
                    elif tokenizer.operation == "/":
                        mathop = Divider()
                    elif tokenizer.operation == "^":
                        mathop = Exponentiation()
                    elif tokenizer.operation == "r":
                        mathop = Rooter()
                    elif tokenizer.operation == "!":
                        mathop = Faculity()

                    else:
                        print("Fehlerhafte Eingabe!")

                    mathop.execute_op(val1=tokenizer.value1, val2=tokenizer.value2)
                    print(mathop._result)
                # Wenn ein konkretes Mathe-Objekt erzeugt wurde, kann nun die Berechnung ausgeführt und das
                # Ergebnis angezeigt werden. Das erfolgt nach der Entscheidung, welche Klasse zu instanziieren ist.
                # Hier nutzen wir die Polymorphie, denn jedes konkrete Objekt, das wir erzeugen, ist immer auch
                # ein MathOp-Objekt und kann daher die Methoden execute_op und result (als Property_aufruf!) ausführen.
                # Und ja hier sind dann die möglichen Fehlerfälle abzufangen und eine entsprechende Info auszugeben.

                except OperationException as exception:
                    print(exception)
                except NumberFormatException as exception:
                    print(exception)
                except ZeroDivisionError as exception:
                    print("ERROR: Division durch Null ist nicht erlaubt!")

                #print("\n")
                eingabe = input("`n` eingeben zum beenden, ansonsten beliebige Taste drücken:")
                if eingabe == "n" or eingabe == "N":
                    break
if __name__ == "__main__":
    Calculator.main()
