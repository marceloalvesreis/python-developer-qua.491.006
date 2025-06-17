"""
# TODO - atividade: Crie um programa com o seguinte menu:
- Calcular área de um círculo
- Calcular tamanho de uma circunfêrencia
- Sair do programa
# NOTE - para cada loop, o programa deverá limpar o terminal
"""

#importa biblioteca
import os
import math

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    limpar()
    print("1 - Área do círculo")
    print("2 - Circunferência")
    print("3 - Sair")
    opcao = input("Escolha: ")

    if opcao == '1':
        r = float(input("Raio: "))
        print(f"Área: {math.pi * r**2:.2f}")
    elif opcao == '2':
        r = float(input("Raio: "))
        print(f"Circunferência: {2 * math.pi * r:.2f}")
    elif opcao == '3':
        break
    else:
        print("Opção inválida.")

    input("\nEnter para continuar...")

