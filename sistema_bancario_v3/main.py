# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 10:00:54 2023

    Desafio da DIO
    Sistema Bancário Otimizado
    Modulo 2 - Estrutura de Dados

@author: alvar
"""

import classes_bancarias


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
    
    
    
    
  
   
def cadastro_usuario(usuarios, cpf):
       
    print("\n\t=== Seção de Cadastro do Usuário ===")
    
    #nome, cpf, nascimento, endereco
    print("\tDigite as informações solicitadas a seguir: ")
    nome = input("\tNome completo: ")
    nascimento = input("\tData de nascimento no formado dd/mm/aaaa: ")
    endereco = input("\tEndereço no formato Rua, Nº - Bairro - Cidade/SILHAESTADO: ")
    
    pessoafisica = classes_bancarias.PessoaFisica(nome, cpf, nascimento, endereco)
    
    usuarios.append(pessoafisica)
    
    
    
    
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
    
    numeros_formatados = False
    caracteres_formatados = False
    
    #verificar se o cpf está no formato válido
    if cpf[:3].isnumeric() and cpf[4:7].isnumeric() and cpf[8:11].isnumeric() and cpf[12:].isnumeric():
        numeros_formatados = True
        
    if cpf[3] == '.' and cpf[7] == '.'and cpf[11] == '-':
        caracteres_formatados = True
        
    if numeros_formatados and caracteres_formatados:
        #retira o ponto e o traço da string CPF
        cpf = cpf.replace('-', '')
        cpf = cpf.replace('.', '')
        
        return cpf
        
    else:
        return "invalido"
    

    
    
def existe_cpf(usuarios, cpf):
        usuario_cadastrado = False
        
        for usuario in usuarios:
            if usuario.cpf == cpf:
                usuario_cadastrado = True
                
        return usuario_cadastrado
                
        



        
def informacoes_do_usuario():
    
    cpf = input("CPF (000.000.000-00): ")
    
    cpf = tratar_cpf(cpf)
    

    
    # usuario = {
    #     "nome":nome,
    #     "nascimento":nascimento,
    #     "cpf":cpf,
    #     "endereco":endereco
    #     }
    
    # return usuario        
        
        
        
        
        

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
            
        
            while True:
                
                print("\n\n\t=== Cadastro de usuário === ")
            
            
                #pedir cpf do usuario
                print("\t[q] para Voltar ou Digite o CPF para consulta.")
                print("\t... Formatação do CPF (000.111.222-33)")
                
                cpf = input("\n\tadmin => ")
                
                if cpf == 'q':
                    break
                else:
                    cpf = tratar_cpf(cpf)
                
            
                if cpf == "invalido":
                    print("\n\t@@@ CPF inválido.")
                    print("\t@@@ Digite um CPF no formato 000.000.000-00).")
                    continue
                
                
                usuario_cadastrado = existe_cpf(usuarios, cpf)


                if usuario_cadastrado:
                    print("\n\tUsuário já possui cadastro no sistema.")
                    
                else:
                    cadastro_usuario(usuarios, cpf)
                    print("\n\tO cadastro do usuário foi realizado com suscesso.")
            
        elif opcao == "c":
            
            while True:
                
                print("\n\n\t=== Cadastro de Conta === ")
            
            
                #pedir cpf do usuario
                print("\t[q] para Voltar ou Digite o CPF para consulta.")
                print("\t... Formatação do CPF (000.111.222-33)")
                
                cpf = input("\n\tadmin => ")
                
                if cpf == 'q':
                    break
                else:
                    cpf = tratar_cpf(cpf)
                
            
                if cpf == "invalido":
                    print("\n\t@@@ CPF inválido.")
                    print("\t@@@ Digite um CPF no formato 000.000.000-00).")
                    continue
                
                
                usuario_cadastrado = existe_cpf(usuarios, cpf)


                if usuario_cadastrado:
                    for usuario in usuarios:
                        if usuario.cpf == cpf:
                            
                            numero_da_conta = len(contas)+1
                            
                            conta = classes_bancarias.Conta.nova_conta(usuario, numero_da_conta)
                            
                            contas.append(conta)
                            usuario.adicionar_conta(conta)
                            
                            print(conta)
                    
                else:
                    print("\n\t@@@ O cliente não possui cadastro no sistema.")
                    print("\t@@@ Realize o cadastro do cliente para criar uma conta.")
            
        elif opcao == "lu":
            
            if len(usuarios)==0:
                print("\n\t=== Lista de usuários vazia. ===")
            else:
                print()
                for indice, usuario in enumerate(usuarios):                
                    print(f'=== [{indice+1}]\n{usuario}]')
            
        elif opcao == "lc":
            
            if len(contas)==0:
                print("\n\t=== Lista de contas vazia. ===")
            else:
                print()
                for indice, conta in enumerate(contas):
                    print(f'=== [{indice+1}]\n{conta}')
            
            
        elif opcao == "q": #volta ao menu principal
        
            return "seção_administrador_encerrada"
            
        else:
            print("\n\tOperação inválida. ")
            print("\n\tPor favor, selecione novamente a operação desejada.")
            
            
            
            
            

def menu_usuario(usuarios):
    
    # saldo = 0
    # limite = 500
    # extrato = ""
    # numero_saques = 0
    # LIMITE_SAQUES = 3
    
    menu_usuario = """
    
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    
    user => """
    
    while True:
        
        print("\n\n\t=== Login de Conta === ")
    
    
        #pedir cpf do usuario
        print("\t[q] para Voltar ou Digite o CPF para entrar.")
        print("\t... Formatação do CPF (000.111.222-33)")
        
        cpf = input("\n\tuser => ")
        
        if cpf == 'q':
            return "seção_usuario_encerrada"
        else:
            cpf = tratar_cpf(cpf)
        
    
        if cpf == "invalido":
            print("\n\t@@@ CPF inválido.")
            print("\t@@@ Digite um CPF no formato 000.000.000-00).")
            continue
        
        
        usuario_cadastrado = existe_cpf(usuarios, cpf)
        
        if usuario_cadastrado:
            
            indice_usuario = 0
            
            for indice, usuario in enumerate(usuarios):
                
                if usuario.cpf == cpf:
                    
                    # posição do usuario na memória
                    indice_usuario = indice
            
            # número da conta do usuário
            conta = int(input("Digite o número da conta: "))
            
            
            conta_encontrada = False
            
            indice_conta = 0
            # usuarios[indice_usuario] -> conta para login
            for indice, cont in enumerate(usuarios[indice_usuario].contas):
                if cont.numero == conta:
                    conta_encontrada = True
                    indice_conta = indice
                    
            # usuario: usuarios[indice_usuario]
            # conta: usuarios[indice_usuario].contas[indice_conta]
            
            if conta_encontrada:
                
                print("Login realizado com sucesso.")
                        
                while True:
                    
                    opcao = input(menu_usuario)
                        
                    if opcao == "d":
                        
                        valor = float(input("\n\tInforme o valor do depósito: "))
                        depositou = usuarios[indice_usuario].contas[indice_conta].depositar(valor)
                        
                        if depositou:
                            print("\tDeposito concluído com sucesso.")
                        else:
                            print("\t@@@ Erro de valor.")
                            
                            
                    elif opcao == "s":
                        
                        valor = float(input("\n\tInforme o valor do saque: "))
                        sacou = usuarios[indice_usuario].contas[indice_conta].sacar(valor)
                        
                        if sacou:
                            print("\tSaque concluído com sucesso.")
                        else:
                            print("\t@@@ Erro de valor.")
                        
                    elif opcao == "e":
                        
                        lista_transacoes = usuarios[indice_usuario].contas[indice_conta].historico.transacoes
                        
                        for transacao in lista_transacoes:
                            
                            print("{}\t{}\t{}".format(transacao["data"], transacao["tipo"], transacao["valor"]))
                        
                        print("Saldo: R$", usuarios[indice_usuario].contas[indice_conta].saldo)

                    elif opcao == "q":
                        
                        print("\n\tSeção de usuario encerrada.")
                        return "seção_usuario_encerrada"

                    else:
                        print("\n\tOperação inválida, por favor selecione novamente a operação desejada.")
                        
            else:
                print("\t@@@ Conta não encontrada.")
                        
        else:
            print("\n\t@@@ Usuário não encontrado no sistema.")
            print("\t@@@ Verifique se o número digitado está correto.")
            print("\t@@@ Caso o problema persista, procure seu gerente.")
    

            
            
            

def main():
    
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
            
            opcao = menu_usuario(usuarios)
            
        elif opcao == "seção_usuario_encerrada":
            
            continue
        
        elif opcao == "a":
            
            menu_administrador(usuarios, contas)
            
        elif opcao == "seção_administrador_encerrada":
            
            continue
            
        elif opcao == "q":
            
            print("\n\tPrograma encerrado.")
            break
        
        else:
            print("\n\tOperação inválida. ")
            print("\n\tPor favor, selecione novamente a operação desejada.")

main()