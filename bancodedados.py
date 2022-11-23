import funcaoconectar as bd

conexao, cursor = bd.conectar()

nome = input("Digite o nome do herói/vilão\n")
nome_civil = input("Digite o nome civil do herói/vilão\n")
tipo_numerico = input("Tecle 1 para herói(na) ou 2 vilão(ã)")

sql = 'SELECT MAX(pessoa_id)+1 FROM pessoas'
cursor.execute(sql)
pessoa_id = cursor.fetchone()[0]
pessoas = cursor.fetchall()

if tipo_numerico == "1":
  tipo = "Herói(na)"
else:
  tipo_numerico = "vilão(ã)"

sql = f"INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES ({pessoa_id}, '{nome}', '{nome_civil}', '{tipo}')"

for pessoa in pessoas:
  print(f"Nome: {pessoa[1]} ({pessoa[3]})")

cursor.execute(sql)
conexao.commit()
cursor.close()



