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

nome = input("Digite seu nome: ")
idade = int(input("\nDigite sua idade: "))
genero = input("\nDigite seu gênero(F para feminino e M para masculino):")

print("\nSeu nome é:{}".format(nome))
print("\nSua idade é:{}".format(idade))
print("\nSeu gênero é:{}".format(genero))
dobro = idade * 2 

#If e Else

print("\nO dobro da sua idade é: {}".format(dobro))

if idade >= 18:
  print("\nVocê é maior de idade, já pode beber ou dirigir!")
else:
  print("\nVocê é menor de idade, não pode beber ou dirigir!")

if idade >=18 and genero == "M":
  print("\nVocê deve ir ao serviço militar!")
else:
  print("\nVocê não precisa ir ao serviço militar!")
  