#!/usr/bin/env python3

class ContaBancaria(object):
    VALOR_INVALIDO = 'Valor muito alto, consulte seu gerente!'

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