import oracledb
import os
from dotenv import load_dotenv

def conectar_db():
    load_dotenv()

    try:
        conexao = oracledb.connect(
            user = os.getenv("DB_USUARIO"),
            password = os.getenv("DB_SENHA"),
            dsn = os.getenv("DB_DSN"),
            mode = oracledb.SYSDBA
        )
        print("Conexão deu certo com o Oracle Database!")
        return conexao
        
    except oracledb.Error as e:
        #retorna um objeto como erro com tuplas, entao:
        erro_obj, = e.args
        print(erro_obj.message)