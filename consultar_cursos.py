import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('cursos.db')
cursor = conn.cursor()

# Consultar todos os cursos
cursor.execute("SELECT * FROM cursos")
cursos = cursor.fetchall()

for curso in cursos:
    print(f"ID: {curso[0]}, Título: {curso[1]}, Descrição: {curso[2]}, Preço: {curso[3]}, Conteúdo: {curso[4]}")

# Fechar a conexão
conn.close()
