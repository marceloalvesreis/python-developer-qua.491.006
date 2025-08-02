"""
# TODO - atividade: Crie um programa de aplicativo de banco, onde:
- O usuário cria uma conta no banco com os seguintes dados:
-- Titular da conta
-- CPF do titular
-- Agência
-- Número da conta
-- Saldo
O usuário pode fazer no programa:
- Consultar dados
- Depositar valor
- Sacar valor
- Imprimir extrato (entende-se: gerar arquivo com os dados da conta)
- Sair do programa
"""

# criar a conta bancária
def criar_conta():
    print("Criação de Conta")
    titular = input("Nome do titular: ")
    cpf = input("CPF do titular: ")
    agencia = input("Número da agência: ")
    numero_conta = input("Número da conta: ")
    saldo = float(input("Saldo inicial: R$ "))
    return {
        'titular': titular,
        'cpf': cpf,
        'agencia': agencia,
        'numero_conta': numero_conta,
        'saldo': saldo
    }

# consultar os dados da conta
def consultar_conta(conta):
    if conta:
        print(f"\nTitular: {conta['titular']}")
        print(f"CPF: {conta['cpf']}")
        print(f"Agência: {conta['agencia']}")
        print(f"Número da Conta: {conta['numero_conta']}")
        print(f"Saldo: R$ {conta['saldo']:.2f}")
    else:
        print("Você precisa criar uma conta primeiro!")

#  depositar na conta
def depositar(conta):
    if conta:
        valor = float(input("Digite o valor do depósito: R$ "))
        conta['saldo'] += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Você precisa criar uma conta primeiro!")

# sacar da conta
def sacar(conta):
    if conta:
        valor = float(input("Digite o valor do saque: R$ "))
        if valor <= conta['saldo']:
            conta['saldo'] -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente!")
    else:
        print("Você precisa criar uma conta primeiro!")

# imprimir o extrato
def gerar_extrato(conta):
    if conta:
        print(f"\nExtrato da Conta {conta['numero_conta']}")
        print(f"Titular: {conta['titular']}")
        print(f"Saldo Atual: R$ {conta['saldo']:.2f}")

# Função principal 
def menu():
    conta = None
    while True:
        print("\n--- Menu ---")
        print("1. Criar conta bancária")
        print("2. Consultar dados da conta")
        print("3. Depositar valor")
        print("4. Sacar valor")
        print("5. Gerar extrato")
        print("6. Sair")
        
        opcao = input("Escolha uma opção (1-6): ")

        if opcao == '1':
            conta = criar_conta()
            print("Conta criada com sucesso!")
        elif opcao == '2':
            consultar_conta(conta)
        elif opcao == '3':
            depositar(conta)
        elif opcao == '4':
            sacar(conta)
        elif opcao == '5':
            gerar_extrato(conta)
        elif opcao == '6':
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Rodar o menu
if __name__ == "__main__":
    menu()