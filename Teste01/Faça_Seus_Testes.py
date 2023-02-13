#Faça os testes e modificações que deseja adicionar
#no sorteio 01



pessoas = dict()
dados = list()
v = 0
n = int(input("Quantas pessoas serão registradas?"))
while True:
    dados.append(str(input("Nome:")))
    dados.append(int(input("Idade:")))
    dados.append(str(input("Sexo:")))
    dados.append(str(input("Gmail:")))
    print("-=" * 25)
    v += 1
    if v == n:
        break