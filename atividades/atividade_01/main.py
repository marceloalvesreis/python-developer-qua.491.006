# laço de reptição
while True:
    # tratamento de exeção
    try:
        # entrada de dados
        etanol = float(input("Informe o valor do etanol: R$ ").replace(",","."))
        gasolina = float(input("Informe o valor da gasolina: R$ ").replace(",","."))
        calculo = (etanol/gasolina)*100
        result = "gasolina" if calculo > 70 else "etanol"
    
    
        print(f"Compensa abastecer com {result}.")


        opcao = input("Deseja refazer o cálculo? (s/n)").Lower().strip()
        match opcao:
            case "s":
                continue
            case "n":
                break
            case _:
                print("Opcao inválida")
                continue
    except Exception as e:
        print(f"Não foi possível executar operação. {e}.")
    continue
