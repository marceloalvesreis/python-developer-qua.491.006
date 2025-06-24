# Lista
itens = [
    "Chocolate",
    "Feijão",
    "Arroz",
    "Macarrão",
    "Biscoito",
    "Ovos", 
    "Leite",
    "Frango"
]

# Exibe a lista de compras
for i in range(len(itens)):
    print(f"Índice {i}: {itens[i]}.")

# Usuário informa o índice a ser alterado
try:
    i = int(input("Informe a posição do índice a ser alterado: "))

    if 0 <= i < len(itens):
        novo_valor = input("Informe o novo valor: ").capitalize().strip()
        itens[i] = novo_valor
        print("Item alterado com sucesso!")
    else:
        print("Índice inválido.")
        
except Exception as e:
    print(f"Não foi possível alterar o item da lista. Erro: {e}")

finally:
    print("\nLista atualizada:")
    for i in range(len(itens)):
        print(f"Índice {i}: {itens[i]}.")
