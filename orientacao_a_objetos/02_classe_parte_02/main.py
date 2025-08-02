# classe
class Pessoa:
    # construtor
    def __init__(self, nome, idade, telefone, cpf, email):
        # atributos 
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.cpf = cpf
        self.email = email

    # método de ação
    def apresentar(self):
        return f"Olá, meu nome é {self.nome}, tenho {self.idade} anos, meu telefone é {self.telefone}, meu cpf é {self.cpf} e meu email é {self.email}."
    
# algoritmo principal
if __name__ == "__main__":
    # instanciar classe
    usuario = Pessoa(
        nome = "Marcelo Alves",
        idade = 17,
        telefone = "(61) 9 55559999",
        cpf = "123.456.789-00",
        email = "marcelo@gmail.com"
    )

    try:
        # input 
        usuario.nome = input("Informe seu nome: ").strip().title()
        usuario.idade = int(input("Informe sua idade: "))
        usuario.telefone = input("Informe seu telefone: ").strip()
        usuario.cpf = input("Informe seu CPF: ").strip()
        usuario.email = input("Informe seu email: ").strip().lower()

        # chama o método
        print(usuario.apresentar())
    except Exception as e:
        print(f"Erro. {e}.")