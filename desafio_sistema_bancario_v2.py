# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 10:00:54 2023

    Desafio da DIO
    Sistema Bancário Otimizado
    Modulo 2 - Estrutura de Dados

@author: alvar
"""

def deposito(saldo, valor, extrato, /):
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato
    
    
    
    
    
def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    LIMITE_SAQUES = 3

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES
    


    if excedeu_saldo:
        print("\n\tOperação falhou! Você não tem saldo suficiente.")


    elif excedeu_limite:
        print("\n\tOperação falhou! O valor do saque excede o limite.")


    elif excedeu_saques:
        print("\n\tOperação falhou! Número máximo de saques excedido.")


    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1


    else:
        print("Operação falhou! O valor informado é inválido.")


    return saldo, extrato, numero_saques





def imprimir_extrato(saldo, /, *, extrato):
    
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    
    
    
    
  
   
def cadastro_usuario(usuarios,*, nome, nascimento, cpf, endereco):
    '''
    Parameters
    ----------
    nome : str
        Nome do usuário.
    nascimento : str
        Data de nascimento no formato "22/11/1993".
    cpf : str
        CPF no formato "000.233.322-13".
    endereco : str
        Endereço no formato "Rua Joao Nabuco, 333 - Bairro - Cidade/SP.

    Returns
    -------
    None

    '''
    
    
    #tratar cpf
    cpf = cpf.replace('-', '')
    cpf = cpf.replace('.', '')
    
    
    #verificar se o cpf já existe na lista de usuários
    for usuario in usuarios:
        
        if usuario["cpf"] == cpf:
            
            print(f"O CPF {cpf} já possui cadastro no sistema.")
            
            #se o cpf já existe, não altera nada e retorna
            return None
    
    
    #caso o cpf não exista,  o cadastro é realizado
    usuario = {"nome":nome, "nascimento":nascimento, "cpf":cpf, "endereco":endereco}
    usuarios.append(usuario)
    
    #confirmação de cadastro
    print("Cadastro realizado com sucesso!")
    
    
    
    
    
    
    
def cadastro_conta(usuarios, contas, cpf):
    
    cpf = tratar_cpf(cpf)
    
    possui_cadastro = False
    
    #verificar se o usuário já possui
    for indice, usuario in enumerate(usuarios):
        
        if usuario["cpf"] == cpf:
            
            possui_cadastro = True
            indice_do_usuario = indice
    
    if possui_cadastro:
        
        agencia = "0001"
        numero_da_conta = len(contas) + 1
        usuario_da_conta = usuarios[indice_do_usuario]["nome"]
        
        conta = {
            "agencia":agencia,
            "numero_da_conta":numero_da_conta,
            "usuario_da_conta":usuario_da_conta
            }
        
        if "contas" in usuarios[indice_do_usuario]:
            usuarios[indice_do_usuario]["contas"].append(numero_da_conta)
        else:
            usuarios[indice_do_usuario]["contas"] = []
            usuarios[indice_do_usuario]["contas"].append(numero_da_conta)
        
        print(conta)
        
        contas.append(conta)
        
        
        
    else:
        print("\n\tO CPF não possui cadastro. \n\tRealize o cadastro do novo usuário.")
        
        
    


    
def tratar_cpf(cpf):
    #tratar cpf
    cpf = cpf.replace('-', '')
    cpf = cpf.replace('.', '')
    
    return cpf    





        
def informacoes_do_usuario():
    
    nome = input("Nome completo: ")
    nascimento = input("Nascimento (dd/mm/aaaa): ")
    cpf = input("CPF (000.000.000-00): ")
    endereco = input("Endereco (Rua Exemplo, Nº - Bairro - Cidade/ESTADO): ")
    
    cpf = tratar_cpf(cpf)
    
    usuario = {
        "nome":nome,
        "nascimento":nascimento,
        "cpf":cpf,
        "endereco":endereco
        }
    
    return usuario        
        
        
        
        
        

def menu_administrador(usuarios, contas):

    menu_administrador = """
    
    [u] Cadastrar Usuário
    [c] Cadastrar Conta
    [lu] Imprimir Lista de Usuarios
    [lc] Imprimir Lista de Contas
    [q] Voltar
    
    admin => """

    while True:
        
        opcao = input(menu_administrador)
        
        
        if opcao == "u": #entra na seção de cadastro
            
            print("Cadastro de usuário")
            
            #funçao para pedir as informações do usuário
            usuario = informacoes_do_usuario()
            
            #função para cadastrar o usuário
            cadastro_usuario(usuarios,**usuario)
            
        elif opcao == "c":
            
            print("\n\t=== Cadastro de Conta ===")
            
            cpf = input("\n\tDigite o CPF do titular da conta: ")
            
            cadastro_conta(usuarios, contas, cpf)
            
            print("\n\t=========================")
            
        elif opcao == "lu":
            
            if len(usuarios)==0:
                print("\n\t=== Lista de usuários vazia. ===")
            else:
                print()
                for indice, usuario in enumerate(usuarios):                
                    print(indice+1, usuario)
            
        elif opcao == "lc":
            
            if len(contas)==0:
                print("\n\t=== Lista de contas vazia. ===")
            else:
                print()
                for indice, conta in enumerate(contas):
                    print(indice+1, conta)
            
            
        elif opcao == "q": #volta ao menu principal
            
            break
            
            
            
            
            

def menu_usuario():
    
    saldo = 0
    limite = 500
    extrato = ""
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
            
            
            
            
            

def menu():
    
    usuarios = []
    contas = []
    
    menu_principal = """
        
    [u] Usuário
    [a] Administrador
    [q] Sair
    
    => """

    while True:
        
        opcao = input(menu_principal)
        
        if opcao == "u":
            
            menu_usuario()
            
        elif opcao == "a":
            
            menu_administrador(usuarios, contas)
            
        elif opcao == "q":
            
            print("\n\tPrograma encerrado.")
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


menu()