# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 08:34:26 2023

@author: alvar
"""

from abc import ABC, abstractmethod, abstractproperty
import datetime



class Cliente():
    
    def __init__(self, endereco):

        self._endereco = endereco
        self._contas = []
        
    @property
    def contas(self):
        return self._contas
        
        
    def realizar_transacao(self, conta, transacao):
        
        print("Realizar Transação.")
        
        if conta in self._contas:
            print("Conta existe.")
            transacao.registrar(conta)
        
        else:
            print("Conta não existe.")
            
    
    
    def adicionar_conta(self, conta):
        
        # print("\tAdicionar Conta.")
        if conta in self._contas:
            print("@@@ Conta já existe.")
            return False
        
        else:
            self._contas.append(conta)
            print("!!! Conta adicionada")
            return True
        
        
    
    def __str__(self):
        
        
        nome_cls = self.__class__.__name__
        dict_items = self.__dict__.items()


        atrib_cls = [f'{chave}={valor}' for chave, valor in dict_items]
        atrib_cls = ', '.join(atrib_cls)
        
        
        return f"{nome_cls}: {atrib_cls}"
    
    
    
class PessoaFisica(Cliente):
    
    def __init__(self, nome, cpf, nascimento, endereco):
        
        self._nome = nome
        self._cpf = cpf
        self._nascimento = nascimento
        super().__init__(endereco)
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def endereco(self):
        return self._endereco
    
    def __str__(self):
        
        return f"\n\tNome: {self._nome}\n\tCPF: {self._cpf}\n\tNascimento: {self._nascimento}\n\tEnd.: {self._endereco}"
    

class Conta():
    
    
    def __init__(self, numero, agencia, pessoafisica, historico, saldo=0):
        
        self._numero = numero
        self._agencia = agencia
        self._cliente = pessoafisica
        self._historico = Historico()
        self._saldo = saldo
    
    @property
    def numero(self):
        return self._numero
    @property
    def saldo(self):
        return self._saldo
    @property
    def historico(self):
        return self._historico
    
    @classmethod
    def nova_conta(cls, pessoafisica, numero):
        
        #criar um objeto historico
        historico = ""
        agencia = "0001"
        return cls(numero, agencia, pessoafisica, historico, saldo=0) 
    
    def sacar(self, valor):
        if (self._saldo - valor) < 0:
            return False
        else:
            self._saldo -= valor
            self._historico.adicionar_transacao(Saque(valor))
            return True
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self._historico.adicionar_transacao(Deposito(valor))
            return True
    
    def __str__(self):
        
        return f"\n\tNum: {self._numero}\n\tAg: {self._agencia}\n\tCPF: {self._cliente.cpf}"

    
class ContaCorrente(Conta):
    
    def __init__(self, numero, agencia, pessoafisica, historico, saldo=0, limite=500, limite_saques=3):
        super().__init__(numero, agencia, pessoafisica, historico, saldo=0)
        self._limite = limite
        self._limite_saques = limite_saques
        
    @property
    def limite(self):
        return self._limite
    
    @property
    def limite_saques(self):
        return self._limite_saques
    

        

class Historico():
    
    def __init__(self):
        self._transacoes = []
    
    
    @property
    def transacoes(self):
        return self._transacoes
    
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
                {
                    "tipo": transacao.__class__.__name__,
                    "valor": transacao.valor,
                    "data": datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
                
                }
            )
        

    def __str__(self):
        
        
        nome_cls = self.__class__.__name__
        dict_items = self.__dict__.items()


        atrib_cls = [f'{chave}={valor}' for chave, valor in dict_items]
        atrib_cls = ', '.join(atrib_cls)
        
        
        return f"{nome_cls}: {atrib_cls}"



class Transacao(ABC):
    
    @abstractmethod
    def registrar(self, conta):
        pass



class Deposito(Transacao):
    
    def __init__(self, valor):
        
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
        
    def registrar(self, conta):
        pass
    
    
    
class Saque(Transacao):
    
    def __init__(self, valor):
        self._valor = valor    
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        pass


    
#Teste de criação do cliente (OK)

# cliente_alvaro = Cliente("Alvaro", "05491669393", "20/11/1990", "Rua Professor Teodorico, 500 - Montese - Fortaleza/CE")
# print(cliente_alvaro)

# print(cliente_alvaro.adicionar_conta(232232323))
# print(cliente_alvaro)

# print(cliente_alvaro.adicionar_conta(232232323))
# print(cliente_alvaro.adicionar_conta(2322232323))
# print(cliente_alvaro.adicionar_conta(23223323))
# print(cliente_alvaro)



#Teste de criação da PessoaFisica (OK)

# nome = "Alvaro"
# cpf = "054.916.693-93"
# nascimento = "20/11/1990"
# endereco = "Rua Professor Teodorico, 500 - Montese - Fortaleza/CE"
# conta = 999999999
# transacao = None



# pessoafisica = PessoaFisica(nome, cpf, nascimento, endereco)

# print(pessoafisica) #Atributos

# pessoafisica.realizar_transacao(conta, transacao) #Conta não existe.

# pessoafisica.adicionar_conta(conta) #Adicionar Conta.

# pessoafisica.realizar_transacao(conta, transacao) #Conta existe.


#Teste da classe Conta
numero = 999999
agencia = "0001"
pessoafisica = "pessoafisica"
historico = "historico"
saldo=0

# conta = Conta(numero, agencia, pessoafisica, historico, saldo)
# print(conta)

# conta = Conta.nova_conta(pessoafisica, numero)
# print(conta)

# historico = Historico()
# print(historico)
# historico.adicionar_transacao("+valor")
# historico.adicionar_transacao("-valor")

# print(historico)