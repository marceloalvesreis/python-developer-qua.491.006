# O valor do etanol ao usuário
etanol = float(input("Digite o valor do etanol (4.29): "))

# O valor da gasolina ao usuário
gasolina = float(input("Digite o valor da gasolina (5.99): "))

# Calcula 70% do valor da gasolina
limite = gasolina * 0.7

# Compara se o etanol é mais vantajoso
if etanol < limite:
    print("Abasteça com ETANOL. Está mais vantajoso.")
else:
    print("Abasteça com GASOLINA. Está mais vantajoso.")
    