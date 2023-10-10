# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 13:30:45 2023

@author: alvar
"""

def menu(usuarios, contas):
    
    menu_principal = """
        
    [u] Usuário
    [a] Administrador
    [q] Sair
    
    => """

    while True:
        
        opcao = input(menu_principal)
        
        if opcao == "u":
            
            menu_conta(contas)
            
        elif opcao == "a":
            
            menu_administrador(usuarios, contas)
            
        elif opcao == "q":
            
            print("\n\tPrograma encerrado.")
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            
            
            
def menu_conta(contas):
    
    tela = """
    =============================
    Digite o número da conta:
        
    => """
    
    sucesso = """
    =============================
    === Bem-vindo ao sistema ====
    =============================
    
    """
    
    falso = """
    =============================
    !!! Conta não encontrada  !!!
    =============================
    
    """
    
    conta = input(tela)
    
    if conta in contas:
        
        print(sucesso)
        menu_usuario(conta)
    
    else:
        print(falso)
        return None


def menu_usuario(conta):
    
    saldo = conta.saldo()
    extrato = conta.historico()
    limite = 500
    numero_saques = 0
    LIMITE_SAQUES = 3
    
    menu_usuario = """
    
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    
    user => """
    
    while True:
        
        opcao = input(menu_usuario)
            
        if opcao == "d":
            
            valor = float(input("\n\tInforme o valor do depósito: "))
            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == "s":
            
            valor = float(input("\n\tInforme o valor do saque: "))
            saldo, extrato, numero_saques = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
            
        elif opcao == "e":
            
            imprimir_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            
            print("\n\tSeção encerrada.")
            break

        else:
            print("\n\tOperação inválida, por favor selecione novamente a operação desejada.")


def imprimir_extrato(saldo, /, *, extrato):
    
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")