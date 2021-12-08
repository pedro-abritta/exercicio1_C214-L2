class Calc:
    def __init__(self, mensagem):
        self.mensagem = mensagem

    def soma(num1, num2):
        return num1 + num2

    def mult(num1, num2):
        return num1 * num2

    def sub(num1, num2):
        return num1 - num2

    def div(num1, num2):
        return num1 / num2

    def mensagem_designP(self):
        print(self.mensagem)

    def altera_mensagem_designP(self, nova):
        self.mensagem = nova

c1 = Calc("Mensagem teste 1!")


