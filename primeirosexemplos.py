#Primeiro projeto em Python!

#comandos de saída e variáveis
#print("Hello World")

#nome = "Diogo Schultz"
#idade = 19

#print(nome)
#print(idade)

#print("Meu nome é:"+nome)
#print("Minha idade é:"+str(idade)+" anos")
#print(f"Meu nome é {nome}")
#print("Minha idade é:{}".format(idade))
#print("Meu nome é:{} e minha idade é:{}".format(nome, idade))

#comando de input

#nome = input("Digite seu nome: ")
#idade = int(input("\nDigite sua idade: "))
#genero = input("\nDigite seu gênero(F para feminino e M para masculino):")

#print("\nSeu nome é:{}".format(nome))
#print("\nSua idade é:{}".format(idade))
#print("\nSeu gênero é:{}".format(genero))
#dobro = idade * 2 

#If e Else

#print("\nO dobro da sua idade é: {}".format(dobro))

#if idade >= 18:
#  print("\nVocê é maior de idade, já pode beber ou dirigir!")
#else:
#  print("\nVocê é menor de idade, não pode beber ou dirigir!")

#if idade >=18 and genero == "M":
#  print("\nVocê deve ir ao serviço militar!")
#else:
#  print("\nVocê não precisa ir ao serviço militar!")

#While

#contador = 1
#while(contador <=10):
#  print(contador)
#contador = contador+1

#laço for
frutas = ["morango", "pera", "laranja"]
#print(frutas[0])
#print(len(frutas))

#incluindo

#frutas.append("manga")
#print(frutas)
#print("Exemplo das frutas com while..")
#frutas.append("uva")

#i=0 #(i de index)
#while(i<len(frutas)):
#  print(frutas[i])
#  i = i + 1

#print("Exemplo das frutas com FOR")
#for fruta in frutas:
#  print(fruta)

#Criação de funções 

#preco = 1999.90

#Calcular apenas 5% de imposto, guardar na variavel imposto e exibir na tela 
#imposto = preco * 0.05
#print(imposto)

#Criar função calcular_imposto () que calcula um imposto de 5% e retorna

#def calcular_imposto(preco_produto):
#  imposto = preco_produto * 0.05
#  return imposto

#imposto2 = calcular_imposto(preco)
#print(imposto2)

valores = [1.99, 24.50, 78.27, 1515.5]

#for valor in valores:
#  print(f"O imposto de {valor} é {calcular_imposto(valor)}")

#Declarar uma função calcula_imposto_aliquota que recebe dois parâmetros: o preço do produto e a alíquota de imposto a ser aplicada e retorna o imposto calculado. Se a aliquota não for informada, utilize 7% como padrão.

def calcular_imposto_aliquota(valor, aliquota = 7):
  imposto = valor * aliquota / 100
  return imposto

for valor in valores:
 print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor, 7)}")
