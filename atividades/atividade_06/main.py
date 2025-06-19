"""
# TODO - atividade: Crie um programa em que o usuário informa 
# um ano e o programa exibe todo o calendário do ano informado
pelo usuário
# NOTE - o usuário poderá informar qualquer ano a partir de 1990
# NOTE - use a biblioteca "calendar"
"""

import calendar

# Estrutura
try:
    ano = int(input("Digite o ano (1990 a 2025): "))
    if ano < 1990 or ano > 2025:
        print("Ano fora do permitido.")
    else:
        print(calendar.TextCalendar().formatyear(ano))
except:
    print("Ano inválido!")
