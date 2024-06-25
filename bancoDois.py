import textwrap

def menu():
    menu = ("""\n  ========= MENU ========
                                    
        1 - DEPÓSITO
        2 - SAQUE
        3 - EXTRATO
        4 - CRIAR USUÁRIO
        5 - CRIAR CONTA 
        6 - LISTAR CONTAS
        0 - SAIR
                \n""")
    return input(textwrap.dedent(menu))
    
    
def depositar(saldo,valor_deposito,extrato,/):  # ANTES DA BARRA = POSICIONAL
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += str(f"""Valor de depósito: R${valor_deposito:.2f} - novo saldo: R$ {saldo:.2f}\n""")
        print("Depósito realizado com sucesso")
    else:
        print("Valor inválido!")
        
    return saldo, extrato

    
def saque(saldo, valor_saque, extrato, limite, limite_saque,/):  # DPS DO * = PASSAR NOMEADO valor = valor e etc...
    
    
    excedeu_saldo = valor_saque > saldo
    excedeu_limite = valor_saque > limite
    excedeu_saques = limite_saque <= 0
    
    if excedeu_saldo:
        print("Saldo insuficiente!")
    elif excedeu_limite:
        print("Valor de saque ultrapassado.")
    elif excedeu_saques:
        print("Saques diários esgotados. Volte amanhã!")
        
    elif valor_saque > 0:
        
        limite_saque -= 1
        saldo -= valor_saque
        extrato += str(f""" Valor de Saque: R${valor_saque:.2f} - novo Saldo: R${saldo:.2f}\n """)
       
   
        print(f"Saque com sucesso")
        print(f"numero de saque: {limite_saque}")
    else:
        print("Operação falhou! Valor inválido")
        
    return saldo, extrato,limite_saque
       
        
def extratos(saldo, /, *, extrato):  # obrigado a passar saldo na SEQUENCIA e extrato NOMEADO
    print("======== EXTRATO ========\n\n")
    print(extrato + "\n")
    print("=================")
    return saldo , extrato

 
def criar_usuario(usuarios):
    cpf = int(input("Digite seu CPF:\n"))
    usuario = filtrar_usuario(cpf,usuarios)
    
    if usuario:
        print("Esse CPF já foi cadastrado")
        return 
        
    
    nome = str(input("Digite seu nome: \n"))
    data_nascimento = str(input("Digite sua data de nascimento (dd-MM-yyyy)\n"))
    endereco = str(input("Digite seu endereço: logradouro - numero - bairro - cidade/sigla estado\n"))
    
    usuarios.append({"nome":nome,"data_nascimento":data_nascimento,"cpf":cpf,"endereco":endereco})
   
    print("Usuário criado com SUCESSO!")
    
   
def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
    
       
def criar_conta(agencia,numero_conta,usuarios):
    cpf = int(input("Informe o CPF do usuario: \n"))
    usuario = filtrar_usuario(cpf,usuarios)
    
    if usuario:
        print("Conta criado com SUCESSO")
        return {"agencia":agencia, "numero_conta":numero_conta,"usuario":usuario}
    
    print("Usuario não encontrado, fluxo de criação de conta encerrado")
    
    
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
    
    
def main():
    print("Olá, bem vindo ao seu Banco Online!")
    
    saldo = 0
    extrato = """ """
    AGENCIA = "0001"
    limite_saque = 3
    limite = 500
    usuarios = []
    contas = []
    op = "-1"


    while op != "0":
        
        op = menu()
        
        if op == "1":
            valor_deposito = float(input("Digite o valor de depósito!\n"))
            saldo,extrato =  depositar(saldo,valor_deposito,extrato)
        
        elif op == "2":
            valor_saque = float(input("Digite o valor de Saque!\n"))
            saldo, extrato,limite_saque = saque(saldo,valor_saque,extrato,limite,limite_saque)
            
            
        elif op == "3":
            extratos(saldo,extrato=extrato)
            
        elif op == "4":
            criar_usuario(usuarios)
            
        elif op =="5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA,numero_conta,usuarios)
            
            if conta:
                contas.append(conta)
            
        elif op =="6":
            listar_contas(contas)
            
        elif op == "0":
            print("Obrigado, volte sempre")
            
        else:
            print("opção inválida!")
            
     

    
    

main()    

    
    

