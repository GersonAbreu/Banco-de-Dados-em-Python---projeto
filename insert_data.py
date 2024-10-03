import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('cursos.db')
cursor = conn.cursor()

# Inserir um usuário
cursor.execute('''
INSERT INTO usuarios (nome, email, senha, role) 
VALUES (?, ?, ?, ?)
''', ('Fabiane', 'fabiane@exemplo.com', 'senha_segura_hash', 'admin'))

# Inserir um curso
cursor.execute('''
INSERT INTO cursos (titulo, descricao, preco, conteudo) 
VALUES (?, ?, ?, ?)
''', ('Curso de Finanças Pessoais', 'Um curso completo sobre como gerenciar suas finanças pessoais.', 299.99, 'link_para_conteudo'))

# Inserir uma compra
cursor.execute('''
INSERT INTO compras (usuario_id, curso_id, data_compra, valor_pago) 
VALUES (?, ?, ?, ?)
''', (1, 1, '2024-10-03', 299.99))

# Salvar as alterações e fechar a conexão
conn.commit()
conn.close()

print("Dados inseridos com sucesso!")
