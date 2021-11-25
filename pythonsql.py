import pyodbc #importar biblioteca
import pandas as pd

#variável da conexão
dados_conexao = ( 
    "Driver={SQL Server};"
    "Server=DESKTOP-L2KJSO8;" #pode ser código IP...
    "Database=Banco_Dados_ST1;" #nome do banco de dados, e não da tabela!
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

cursor = conexao.cursor()

#takes upto 12 minutes
rows = cursor.execute("select top 3 * from ST1 ").fetchall() 

#Read cursor data into Pandas dataframe.....Takes forever!
df = pd.DataFrame([tuple(t) for t in rows]) 
print(df)