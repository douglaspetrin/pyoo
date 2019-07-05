#!/usr/bin/env python3

class ContaBancaria(object):
    def __init__(self):
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

class Investimentos(ContaBancaria):
    def renda_fixa(self):
        return self.saldo * 1.01

    def renda_variavel(self, hipotese):
        return self.saldo * hipotese
