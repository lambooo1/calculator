import ast
from exceptions import OperationException
from exceptions import NumberFormatException

class Tokenizer:
    def __init__(self):
        self.__value1 = None
        self.__operation = None
        self.__value2 = None
        self.__operations = ['+', '-', '*', '/']

    @property
    def value1(self):
        return self.__value1

    @property
    def value2(self):
        return self.__value2

    @property
    def operation(self):
        return self.__operation

    def add_operation(self, operation):
        if operation not in self.__operations:
            self.__operations.append(operation)
        else:
            print("Zeichen " + operation + " ist schon Teil der Liste")

    def get_all_operations(self):
        return self.__operations

    def split(self, command_line):
        for sign in self.__operations:
            if sign in command_line:
                # die Zeichenkette entlang dem Operationszeichen auftrennen
                elements = command_line.partition(sign)
                self.__operation = sign
                # sicherstellen, dass es sich um gültige Zahlenwerte handelt
                try:
                    self.__value1 = ast.literal_eval(elements[0].strip())
                except Exception:
                    raise NumberFormatException(elements[0])
                try:
                    self.__value2 = ast.literal_eval(elements[2].strip())
                except Exception:
                    raise NumberFormatException(elements[2])
                return
        raise OperationException()

if __name__ == "__main__":
    t = Tokenizer()
    print(t.get_all_operations())
    t.add_operation('+')
    t.add_operation('^')
    print(t.get_all_operations())
    try:
        t.split("3.25/7.568")
        #
        print(t.value1)
        print(t.operation)
        print(t.value2)
    except OperationException as exception:
        print(exception)
    except NumberFormatException as exception:
        print(exception)
