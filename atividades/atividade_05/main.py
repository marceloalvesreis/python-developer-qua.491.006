# bibliotecas
import os
import datetime
from datetime import date

# declaração de variáveis
data = date.today().strftime("%d/%m/%Y")
hora = datetime.datetime.now().strftime("%H:/%M:%S")

# filmes das salas
sala1 = "A roda quadrada"
sala2 = "A volta dos que não forma"
sala3 = "Poeira em alto mar"
sala4 = "As tranças do rei careca"
sala5 = "A vingança do peixe frito"

# tratamento de exeção
try:
    nome = input("Informe seu nome: ").title().strip()
    idade = int(input("Informe sua idade: "))

    while True:
        print(f"{'-'*20} CINE COBRA {'-'*20}")
        print(f"Sala 1 - {sala1} - livre")
        print(f"Sala 2 - {sala2} - 12 anos")
        print(f"Sala 3 - {sala3} - 14 anos")
        print(f"Sala 4 - {sala4} - 16 anos")
        print(f"Sala 5 - {sala5} - 18 anos")
        sala = input("Informe o número da sala desejada: ").strip()
        os.system("cls" if os.name == "nt" else "clear")
        match sala:
            case "1":
                idade_minima = 0
                filme = sala1
            case "2":
                idade_minima = 12
                filme = sala2
            case "3":
                idade_minima = 14
                filme = sala3
            case "4":
                idade_minima = 16
                filme = sala4
            case "5":
                idade_minima = 18
                filme = sala5
            case _:
                print("Sala inexistente. Favor escolher outra sala. ")
                continue
        if idade >= idade_minima:
            print(f"{'-'*20} INGRESSO CINE COBRA {'-'*20}\n")
            print(f"{'-'*60}\n")
            print(f"Filme: {filme} - {idade_minima}")
            print(f"Ingresso comprado por {nome} no dia {data} às {hora}.")
            print("TENHA UM BOM FILME!!! =D")
            print(f"{'-'*60}")
            break
        else:
            print(f"{nome} não possui a idade mínima para ver {filme}.")
            print(f"Favor escolher outro filme.")
            continue
except Exception as e:
    print(f"Não foi possível comprar ingresso. {e}.")