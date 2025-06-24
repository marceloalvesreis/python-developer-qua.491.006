"""
# TODO - atvidade: Crie um programa que faça as seguintes operações:
- Cadastre novo nome na lista
- Liste todos os nomes na lista
- Pesquise por um nome na lista
- Altere um nome na lista
- Exclua um nome na lista
- Sair do programa
# NOTE - a lista deve começar vazia. Exemplo: lista = []
"""

lista=[]
while True:
 print("1-Cadastrar\n2-Listar\n3-Pesquisar\n4-Alterar\n5-Excluir\n6-Sair")
 op=input("Escolha: ")
 if op=="1": lista.append(input("Nome: ").capitalize().strip())
 else:
  if op=="2":
   if len(lista)==0: print("Lista vazia.")
   else:
    for i,n in enumerate(lista): print(f"{i}: {n}")
  else:
   if op=="3":
    nome=input("Pesquisar: ").capitalize().strip()
    print(f"{nome} está na lista." if nome in lista else "Nome não encontrado.")
   else:
    if op=="4":
     i=input("Índice para alterar: ")
     if i.isdigit():
      i=int(i)
      if 0<=i<len(lista): lista[i]=input("Novo nome: ").capitalize().strip()
      else: print("Índice inválido.")
     else: print("Digite número válido.")
    else:
     if op=="5":
      i=input("Índice para excluir: ")
      if i.isdigit():
       i=int(i)
       if 0<=i<len(lista): del lista[i]
       else: print("Índice inválido.")
      else: print("Digite número válido.")
     else:
      if op=="6": print("Saindo..."); break
      else: print("Opção inválida.")
