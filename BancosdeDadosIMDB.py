from model.Pessoa import Pessoa
from database.Database import Database
from dao.PessoaDAO import PessoaDAO

diogo = Pessoa(1, "Diogo Rafael Schultz")
print(diogo)
print(diogo.nome)

db = Database()

pessoaDAO = PessoaDAO(db.conexao, db.cursor)

pessoas = pessoaDAO.getAll()
for pessoa in pessoas:
  print(pessoa)

