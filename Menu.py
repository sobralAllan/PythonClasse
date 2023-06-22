from Exercicios import Exercicios


class Menu:
    def __init__(self):
        self.prin = Exercicios
        self.num1 = float(0)
        self.num2 = float(0)

    def coletar(self):
        print("Informe um número: ")
        self.num1 = float(input())

        print("Informe outro número: ")
        self.num2 = float(input())

    def imprimir(self):
        print("Soma: {}".format(self.prin.somar(self, self.num1,self.num2)))
        print("Subtração: {}".format(self.prin.subt(self, self.num1, self.num2)))
        print("Multiplicação: {}".format(self.prin.mult(self,self.num1,self.num2)))
        print("Divisão: {}".format(self.prin.divi(self,self.num1,self.num2)))