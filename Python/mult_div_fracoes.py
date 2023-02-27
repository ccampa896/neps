class Fracao:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    # TODO: Implemente o operador de multiplicação.
    def __mul__(self, fracao):
        return Fracao(self.numerador * fracao.numerador, self.denominador * fracao.denominador)

    # TODO: Implemente o operador de divisão.
    def __truediv__(self, fracao):
        return Fracao(self.numerador * fracao.denominador, self.denominador * fracao.numerador)


if __name__ == "__main__":

    a_numerador, a_denominador = map(int, input().split())
    b_numerador, b_denominador = map(int, input().split())
    op = input()

    a = Fracao(a_numerador, a_denominador)
    b = Fracao(b_numerador, b_denominador)

    if op == "M":
        c = a * b
    else:
        c = a / b

    print(c.numerador, c.denominador)

