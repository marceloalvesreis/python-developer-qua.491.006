"""
# TODO - atividade: Crie um programa que receba do usuário, o nome, o peso em kg, e a altura em metros, e calcule o valor do IMC (Índice de Massa Corporal).
O programa deve mostrar o valor do IMC arredondado para 2 casas decimais e mostrar o diagnóstico do usuário com base nos seguintes valores:
- Caso o IMC seja menor que 18.5 = abaixo do peso
- Caso o IMC seja maior ou igual a 18.5 e menor que 25 = peso ideal.
- Caso o IMC seja maior ou igual a 25 e menor que 30 = acima do peso.
- Caso o IMC seja maior ou igual a 30 e menor que 35 = obeso.
- Caso o IMC seja maior ou igual a 35 e menor que 40 = obesidade nível 2.
- Caso o IMC seja maior ou igual a 40 = obesidade mórbida.
# NOTE - o usuário deverá informar o encerramento do programa, ou seja, ele poderá repetir o cálculo quantas vezes quiser
"""

while True:
    nome = input("Digite seu nome: ")
    if nome.lower() == 'sair':
        print("Encerrando o programa. Até mais!")
        break

    while True:
        peso = input("Digite seu peso em kg: ")
        try:
            peso = float(peso)
            break  
        except Exception as e:
            print("Por favor, digite um número válido para o peso.")

    while True:
        altura = input("Digite sua altura em metros: ")
        try:
            altura = float(altura)
            break  
        except Exception as e:
            print("Por favor, digite um número válido para a altura.")

    imc = peso / (altura **2)
    imc_arredondado = round(imc, 2)

    if imc < 18.5:
        diagnostico = "abaixo do peso"
    elif 18.5 <= imc < 25:
        diagnostico = "peso ideal"
    elif 25 <= imc < 30:
        diagnostico = "acima do peso"
    elif 30 <= imc < 35:
        diagnostico = "obeso"
    elif 35 <= imc < 40:
        diagnostico = "obesidade nível 2"
    else:
        diagnostico = "obesidade mórbida"

    print(f"\n{nome}, seu IMC é {imc_arredondado}. Diagnóstico: {diagnostico}.\n")