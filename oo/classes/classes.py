#!/usr/bin/env python3

class ContaBancaria(object):
    VALOR_INVALIDO = 'Valor muito alto, consulte seu gerente!'
    VALOR_MIN = 'O valor mínimo para essa operação é R$ 50'

    def __init__(self):
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def ted(self, valor):
        if valor >= 900:
            raise Exception(self.VALOR_INVALIDO)
        else:
            self.saldo -= valor
            print(self.saldo)

class Investimentos(ContaBancaria):
    def renda_fixa(self):
        return self.saldo * 1.01

    def renda_variavel(self, hipotese):
        return self.saldo * hipotese

    def cryptocurrency(self, valor):
        if valor <= 50:
            raise Exception(self.VALOR_MIN)
        else:
            super(Investimentos, self).sacar(valor)

class Polimorfismo(Investimentos):
    pass