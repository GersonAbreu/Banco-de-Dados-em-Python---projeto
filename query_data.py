import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('cursos.db')
cursor = conn.cursor()

# Consultar todos os usuários
cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()

print("Usuários:")
for usuario in usuarios:
    print(usuario)

# Consultar todos os cursos
cursor.execute("SELECT * FROM cursos")
cursos = cursor.fetchall()

print("\nCursos:")
for curso in cursos:
    print(curso)

# Consultar todas as compras
cursor.execute("SELECT * FROM compras")
compras = cursor.fetchall()

print("\nCompras:")
for compra in compras:
    print(compra)

# Fechar a conexão
conn.close()
