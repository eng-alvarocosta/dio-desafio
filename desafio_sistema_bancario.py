# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 08:53:33 2023

    Desafio do sistema bancário da DIO.
    Desenvolvedor Python.

@author: alvar
"""

menu = """

    SISTEMA BANCARIO
    -----------------------------

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [f] Fechar sistema
    
    - Digite a letra correspondente à operação desejada.

"""

menu_depositar = """

    [d] Depositar
    -----------------------------
    Digite o valor do depósito: 
"""

menu_saque = """

    [s] Sacar
    -----------------------------
    Digite o valor para saque: 
"""

menu_limite_saques = """
    
    Quantidade de saques diários excedido.
    Você já realizou 3 saques hoje.
    
"""

menu_saque_sucesso = """

    Saque realizado com sucesso.
    
"""

menu_saque_falha = """

    Saldo insuficiente para operação.
    
"""

menu_extrato = """

    [e] Extrato
    -----------------------------
    Impressão do extrato:
        

"""

menu_linha = """
    -----------------------------
"""

menu_fechar_sistema = """
    Operação encerrada.
    Obrigado por usar nossos serviços.
"""

menu_opcao_invalida = """
    (!!) Você não digitou uma opção válida.
    (!!) Por favor, digite uma das opções d, s, e ou f.
"""

menu_sem_saldo = """

    (!!) Atenção! Você não tem limite para saque.

"""

saldo = 0
limite = 500.00
extrato = f''
deposito = 0
saque = 0
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    operacao = input(menu + "\t")
    
    if operacao == 'd':
        
        print(menu_depositar)
        deposito = round(float(input('\tR$')),2)
        
        if deposito > 0:
        
            saldo += deposito
            
            print(menu_linha)
            print(f'\n\tR${deposito} Depositado.')
            
            extrato += (f'\n\t+{deposito:16}')
            
        else:
            print(menu_linha)
            print("\n\tValor inválido. Digite um valor maior que 0.")
            
        
    elif operacao == 's':
        
        if numero_saques == LIMITE_SAQUES:
            
            print(menu_linha)
            print(menu_limite_saques)
        else:
            
            if saldo == 0:
                
                print(menu_linha)
                print(menu_sem_saldo)
                
            else:
                
                print(menu_saque)
                saque = round(float(input('\tR$')),2)
                
                if saque <= saldo:
                    
                    if saque <= 500:
                        
                        print(menu_saque_sucesso)
                        print(f"\tR${saque}")
                        
                        saldo -= saque
                        extrato += f'\n\t-{saque:16}'
                        numero_saques += 1
                        
                    else:
                        
                        print(menu_linha)
                        print(f"\n\n\tLimite máximo para saque: R${limite}")
                        print("\tTente realizar a operação novamente.")
                    
                else:
                    
                    print(menu_saque_falha)
                    
    elif operacao == 'e':
        
        print(menu_linha)
        print(menu_extrato)
        print(extrato)
        print(f'\n\tSaldo: R${saldo:8}')
                    
    elif operacao == 'f':
        
        print(menu_linha)
        print(menu_fechar_sistema)
        break
        
    else:
        
        print(menu_linha)
        print(menu_opcao_invalida)
        