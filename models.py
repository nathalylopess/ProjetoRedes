# from flask_login import UserMixin
# import sqlite3

# BANCO = 'database.db'
# def obter_conexao():
#     conn = sqlite3.connect(BANCO)
#     conn.row_factory = sqlite3.Row
#     return conn

# # classe python - Modelo (acessa o banco)
# class User(UserMixin):
#     id : str
#     def __init__(self, email, senha):
#         self.email = email
#         self.senha = senha
    
#     @classmethod
#     def get(cls, id):
#         conexao = obter_conexao()
#         SELECT = 'SELECT * FROM usuarios WHERE id=?'
#         dados = conexao.execute(SELECT, (id,)).fetchone()
#         user = User(dados['email'], dados['senha'])
#         user.id = dados['id']
#         return user
    
#     @classmethod
#     def get_all(cls):
#         conexao = obter_conexao()
#         SELECT = 'SELECT * FROM usuarios'
#         dados = conexao.execute(SELECT).fetchall()
#         return [dict(dado) for dado in dados]
    
#     @classmethod
#     def get_by_email(cls, email):
#         conexao = obter_conexao()
#         SELECT = 'SELECT * FROM usuarios WHERE email=?'
#         dados = conexao.execute(SELECT, (email,)).fetchone()
#         if dados:    
#             user = User(dados['email'], dados['senha'])
#             user.id = dados['id']
#             return user
#         return None

from flask_login import UserMixin
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash  # Adicionando a importação para hash

BANCO = 'database.db'

def obter_conexao():
    conn = sqlite3.connect(BANCO)
    conn.row_factory = sqlite3.Row
    return conn

# Classe Python - Modelo (acessa o banco)
class User(UserMixin):
    id: str
    
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
    
    @classmethod
    def get(cls, id):
        conexao = obter_conexao()
        SELECT = 'SELECT * FROM usuarios WHERE id=?'
        dados = conexao.execute(SELECT, (id,)).fetchone()
        user = User(dados['email'], dados['senha'])
        user.id = dados['id']
        return user
    
    @classmethod
    def get_all(cls):
        conexao = obter_conexao()
        SELECT = 'SELECT * FROM usuarios'
        dados = conexao.execute(SELECT).fetchall()
        return [dict(dado) for dado in dados]
    
    @classmethod
    def get_by_email(cls, email):
        conexao = obter_conexao()
        SELECT = 'SELECT * FROM usuarios WHERE email=?'
        dados = conexao.execute(SELECT, (email,)).fetchone()
        if dados:    
            user = User(dados['email'], dados['senha'])
            user.id = dados['id']
            return user
        return None

    @classmethod
    def create_user(cls, email, senha):
        # Gera o hash da senha antes de salvar
        hashed_password = generate_password_hash(senha)
        conexao = obter_conexao()
        INSERT = 'INSERT INTO usuarios(email, senha) VALUES (?, ?)'
        conexao.execute(INSERT, (email, hashed_password))
        conexao.commit()
        conexao.close()

    def check_password(self, senha):
        # Verifica se a senha fornecida corresponde ao hash armazenado
        return check_password_hash(self.senha, senha)
