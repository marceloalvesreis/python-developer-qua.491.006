# Tratamento de execeção
try: 
    n = int(input("Informe um número inteiro: "))
    print(f"Número informado: {n}. ")
except Exception as e:
    print(f"Não possível exibir o número. {e}.")
finally:
    print("Programa encerrado com sucesso!")