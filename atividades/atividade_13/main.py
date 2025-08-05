import classe as c
import os 

limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    cc = c.Conta(titular="", cpf="", agencia="", conta="", saldo=0.0)

    # define os valores dos atributos
    cc.titular = input("Informe o nome titular da conta: ").strip().title()
    cc.cpf = input("Informe o CPF do titular: ").strip()
    cc.agencia = "1010-1"
    cc.conta = "10101-1"

    limpar()
    while True:
        print(f"{'-'*20} BANCO COBRA {'-'*20}")
        print("1 - Consultar dados.")
        print("2 - Depositar valor.")
        print("3 - Sacar valor.")
        print("4 - Imprimir extrato.")
        print("5 - Sair do programa.")
        opcao = input("Informe a operação desejada: ").strip()
        limpar()
        match opcao:
            case "1":
                cc.consultar_dados()
                continue
            case "2":
                try:
                    valor = float(input("Informe o valor a ser depositado: R$ ").replace(',', '.'))
                    limpar()
                    if valor > 0:
                        print(f"Depósito efetuado com sucesso. Saldo: R$ {cc.depositar(valor):.2f}")
                    else: 
                        print("Valor do depósito inválido.")
                except Exception as e: 
                    print(f"Erro. {e}.")
                finally:
                    continue
            case "3":
                try:
                    valor = float(input("Informe o valor a ser sacado: R$ ").replace(',', '.'))
                    limpar()
                    if valor > 0:
                        if valor <= cc.saldo:
                            print(f"Saque efetuado com sucesso. Saldo: R$ {cc.sacar(valor):.2f}.")
                        else: 
                            print("Saldo insuficiente.")
                    else:
                        print("Valor do saque inválido.")
                except Exception as e:
                    print(f"Erro. {e}.")
                finally:
                    continue
            case "4":
                try:
                    cc.imprimir_extrato()
                    print("Extrato impresso com sucesso.")
                except Exception as e:
                    print(f"Não foi possível imprimir extrato. {e}.")
                finally:
                    continue
            case "5":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida.")
                continue

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