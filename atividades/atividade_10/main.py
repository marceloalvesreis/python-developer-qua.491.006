"""
# TODO - atividade: Faça um CRUD (Create, Read, Update, Delete) em um JSON
Opções do menu:
- Criar novo arquivo JSON.
- Abrir arquivo JSON.
- Cadastrar novo usuário.
- Listar todos os usuários de um arquivo JSON.
- Pesquisar usuário através de um valor de uma chave de um arquivo JSON.
- Alterar dados de um usuário em um arquivo JSON.
- Deletar usuário de um arquivo JSON.
- Sair do programa
Dados do usuário:
- Nome
- Data de Nascimento
- CPF
- E-mail
-Telefone
- Filme favorito
"""

import json
import os

usuarios = []
nome_arquivo = None
while True:
    usuario = {}

    # menu
    print("1 - Criar novo arquivo")
    print("2 - Abrir arquivo")
    print("3 - Cadastrar novo usuário")
    print("4 - Listar todos os usuários")
    print("5 - Pesquisar usuário por valor de qualquer chave")
    print("6 - Alterar dados de um usuário")
    print("7 - Deletar usuário")
    print("8 - Sair do programa")
    opcao = input("Informe a opção desejada: ").strip()

    match opcao:
        case "1":
            nome_arquivo = input("Informe o nome: ").strip().lower()
            with open(f"{nome_arquivo}.json", "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False, indent=4)
            os.system("cls" if os.name == "nt" else "clear")    
            print("Arquivo salvo com sucesso.")
            continue
        case "2":
            try:
                with open(f"{nome_arquivo}.json", "r", encoding="utf-8") as f:
                    usuarios = json.load(f)
                print("Arquivo aberto com sucesso.")
            except Exception as e:
                print(f"Não foi possível abrir. {e}.")
            
        case "3":
            if nome_arquivo is None:
                print("Crie um arquivo.")
                continue
            
            usuario = {
                "nome": input("Nome: ").strip().title(),
                "data_nascimento": input("Data de nascimento (DD/MM/AAAA): ").strip(),
                "cpf": input("CPF: ").strip(),
                "email": input("E-mail: ").strip().lower(),
                "telefone": input("Telefone: ").strip(),
                "filme_favorito": input("Filme favorito: ").strip().title()
            }

            usuarios.append(usuario)
            with open(f"{nome_arquivo}.json", "w", encoding="utf-8") as f:
                json.dump(usuarios, f, ensure_ascii=False, indent=4)
            print("Cdastro feito com sucesso.")
        case "4":
            if not usuarios:
                print("Nenhum usuário cadastrado.")
            else:
                for i, usuario in enumerate(usuarios, start=1):
                    print(f"Usuário {i}:")
                    for chave, valor in usuario.items():
                        print(f"{chave.capitalize().replace('_', ' ')}: {valor}")
                    print("-"*40)
        case "5":
            chave = input("Informe o nome da chave: ").strip().lower()
            valor = input("Informe o valor a buscar: ").strip().lower()
            encontrado = False
            for usuario in usuarios:
                
        case "6":
            ...
        case "7":
            ...
        case "8":
            print("Programa encerrado.")
            break
        case _:
            print("Opção inválida.")
            continue
        