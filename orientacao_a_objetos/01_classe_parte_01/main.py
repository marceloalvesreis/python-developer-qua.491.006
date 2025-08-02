# classe
class Pessoa:
    # atributos
    nome = "Marcelo Alves"
    idade = 17
    telefone = "(61) 9 55559999"
    cpf = "123.456.789-00"
    email = "marcelo@gmail.com"

    # método
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos, meu telefone é {self.telefone}, meu cpf é {self.cpf} e meu email é {self.email}.")

# programa principal
if __name__ == "__main__":
    # instanciar classe
    usuario = Pessoa()

    # objeto se apresenta
    usuario.apresentar()