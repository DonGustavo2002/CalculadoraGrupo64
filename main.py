# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

class calculadora:
    def __init__(self, num1, num2):
        self.num1 = float(num1)
        self.num2 = float(num2)

    def sumar(self):
        suma = self.num1 + self.num2
        print("el resultado de la suma es: ", suma)

    def restar(self):
        resta = self.num1 - self.num2
        print("el resultado de la resta es: ", resta)

    def multiplicar(self):
        multiplicacion = self.num1 * self.num2
        print("el resultado de la multiplicación es: ", multiplicacion)

    def dividir(self):
        divicion = self.num1 / self.num2
        print("el resultado de la divición es: ", divicion)


num1 = input("ingrese un numero: ")
num2 = input("ingrese un numero: ")

calculadora = calculadora(num1, num2)
calculadora.sumar()
calculadora.multiplicar()
calculadora.restar()
calculadora.dividir()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
