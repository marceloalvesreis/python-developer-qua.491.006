import Pessoa
from dataclasses import dataclass

@dataclass
class PessoaFisica(Pessoa.Pessoa):
    nome: str
    cpf: str
    idade: int

    def __str__(self):
        return f"{'-'*20} Dados pessoais:\n\nNome: {self.nome}\nCPF: {self.cpf}\nIdade: {self.idade}\ne-mail: {self.email}\nTelefone: {self.telefone}\nEndereço: {self.endereco}"
    
    def __len__(self):
        return self.idade