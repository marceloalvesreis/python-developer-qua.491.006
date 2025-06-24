# Lista de cidades
cidades = [
    'Brasília',
    'São Paulo',
    'Rio de Janeiro',
    'Teresina',
    'Belo Horizonte',
    'Palmas'
]

# Exibe a lista e seus respectivos índices
for i in range(len(cidades)):
    print(f"Índice {i}: {cidades[i]}.")

# Tratamento de exceção
try:
    # Usuário informa o nome da nova cidade e a posição
    nova_cidade = input("Informe o nome da nova cidade: ").title().strip()
    i = int(input("Informe a posição da lista onde deseja inserir: "))

    # Verifica se o índice está dentro dos limites da lista
    if 0 <= i <= len(cidades):
        cidades.insert(i, nova_cidade)
        print(f"\nCidade '{nova_cidade}' inserida na posição {i}.")
    else:
        print("Índice inválido. Não foi possível inserir a cidade.")

except Exception as e:
    print(f"Não foi possível inserir item na lista. Erro: {e}")
finally:
    # Re-exibe a lista e suas posições
    print("\nLista atualizada:")
    for i in range(len(cidades)):
        print(f"Índice {i}: {cidades[i]}")
