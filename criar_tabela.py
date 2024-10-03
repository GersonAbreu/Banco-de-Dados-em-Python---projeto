import sqlite3

# Conectar ao banco de dados (será criado se não existir)
conn = sqlite3.connect('cursos.db')
cursor = conn.cursor()

# Criar tabela de Usuários
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL,
    role TEXT NOT NULL CHECK(role IN ('admin', 'aluno'))
)
''')

# Criar tabela de Cursos
cursor.execute('''
CREATE TABLE IF NOT EXISTS cursos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descricao TEXT,
    preco REAL NOT NULL,
    conteudo TEXT
)
''')

# Criar tabela de Compras
cursor.execute('''
CREATE TABLE IF NOT EXISTS compras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    curso_id INTEGER NOT NULL,
    data_compra DATE NOT NULL,
    valor_pago REAL NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (curso_id) REFERENCES cursos(id)
)
''')

# Salvar alterações e fechar conexão
conn.commit()
conn.close()

print("Tabelas criadas com sucesso!")
