
#Dados do Usúario

x=eval(input("Quantas pessoas serão cadastradas: "))

def Cadastro():
  print("\nColoque seus dados\n")

  nome=input("Coloque seu nome: ")
  idade=eval(input("Coloque sua idade: "))
  telefone=input("Coloque seu Telefone: ")
  email=input("Coloque seu email: ")
  print("\nColoque seu endereço")
  rua=input("Coloque seu logradouro: ")
  bairro=input("Coloque seu bairro: ")
  numero=eval(input("Coloque o número da sua casa/prédio: ",))
  print("\n")

  print(nome)
  print(idade)
  print(telefone)
  print(email)
  print(rua)
  print(bairro)
  print(numero,"\n")
  print("Cadastro feito com sucesso")

for b in range(0,x):
  Cadastro()


     