import classes as c

def main():
    proprietario = c.Pessoa(nome="", cpf="", email="", telefone="", endereco="")

    carro = c.Veiculo(modelo="", fabricante="", cor="", placa="", ano="", proprietario="")

    # inputs
    print("DADOS DO PROPRIETARIO:")
    proprietario.nome = input("Informe o nome: ").strip().title()
    proprietario.cpf = input("Informe o CPF: ").strip()
    proprietario.email = input("Informe o e-mail: ").strip().lower()
    proprietario.telefone = input("Informe o telefone: ").strip()
    proprietario.endereco = input("Informe o endereço: ").strip().title()

    print("DADOS DO VEICULO:")
    carro.fabricante = input("Informe o fabricante: ").strip().title()
    carro.modelo = input("Informe o modelo: ").strip().title()
    carro.cor = input("Informe a cor do carro: ").strip()
    carro.placa = input("Informe a placa do carro: ").strip().upper()
    carro.ano = input("Informe o ano do carro: ").strip()

    carro.proprietario = proprietario

    print("\nExibindo os dados do veiculo:\n")
    print(f"Fabricante: {carro.fabricante}")
    print(f"Modelo: {carro.modelo}")
    print(f"Cor do carro: {carro.cor}")
    print(f"Placa do veiculo): {carro.placa}")
    print(f"Ano do veiculo: {carro.ano}")
    print(f"Dados do proprietario do veiculo:\n {carro.info_}")

if __name__ == "__main__":
    main()