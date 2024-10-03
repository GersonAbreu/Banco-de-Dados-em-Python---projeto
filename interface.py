import tkinter as tk
from tkinter import ttk
import sqlite3

# Função para consultar e exibir os cursos na interface
def exibir_cursos():
    conn = sqlite3.connect('cursos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cursos")
    rows = cursor.fetchall()
    for row in tree_cursos.get_children():
        tree_cursos.delete(row)
    for row in rows:
        tree_cursos.insert("", tk.END, values=row)
    conn.close()

# Função para consultar e exibir os usuários na interface
def exibir_usuarios():
    conn = sqlite3.connect('cursos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    rows = cursor.fetchall()
    for row in tree_usuarios.get_children():
        tree_usuarios.delete(row)
    for row in rows:
        tree_usuarios.insert("", tk.END, values=row)
    conn.close()

# Função para adicionar um curso
def adicionar_curso():
    conn = sqlite3.connect('cursos.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cursos (titulo, descricao, preco, conteudo) VALUES (?, ?, ?, ?)", 
                   (titulo_entry.get(), descricao_entry.get(), preco_entry.get(), conteudo_entry.get()))
    conn.commit()
    conn.close()
    exibir_cursos()
    limpar_cursos()  # Limpa os campos após adicionar

# Função para adicionar um usuário
def adicionar_usuario():
    conn = sqlite3.connect('cursos.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome, email, senha, role) VALUES (?, ?, ?, ?)",
                   (nome_entry.get(), email_entry.get(), senha_entry.get(), role_entry.get()))
    conn.commit()
    conn.close()
    exibir_usuarios()
    limpar_usuarios()  # Limpa os campos após adicionar

# Função para deletar um curso
def deletar_curso():
    selected_item = tree_cursos.selection()[0]
    curso_id = tree_cursos.item(selected_item)['values'][0]
    conn = sqlite3.connect('cursos.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cursos WHERE id=?", (curso_id,))
    conn.commit()
    conn.close()
    exibir_cursos()

# Função para buscar cursos
def buscar_curso():
    conn = sqlite3.connect('cursos.db')
    cursor = conn.cursor()
    search_term = busca_entry.get()
    query = f"SELECT * FROM cursos WHERE titulo LIKE ?"
    cursor.execute(query, ('%' + search_term + '%',))
    rows = cursor.fetchall()
    for row in tree_cursos.get_children():
        tree_cursos.delete(row)
    for row in rows:
        tree_cursos.insert("", tk.END, values=row)
    conn.close()

# Função para limpar os campos de entrada de cursos
def limpar_cursos():
    titulo_entry.delete(0, tk.END)
    descricao_entry.delete(0, tk.END)
    preco_entry.delete(0, tk.END)
    conteudo_entry.delete(0, tk.END)

# Função para limpar os campos de entrada de usuários
def limpar_usuarios():
    nome_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    senha_entry.delete(0, tk.END)
    role_entry.delete(0, tk.END)

# Interface
root = tk.Tk()
root.title("Gerenciamento de Cursos e Usuários")

# --- Seção para Cursos ---
tk.Label(root, text="Título").grid(row=0, column=0)
titulo_entry = tk.Entry(root)
titulo_entry.grid(row=0, column=1)

tk.Label(root, text="Descrição").grid(row=1, column=0)
descricao_entry = tk.Entry(root)
descricao_entry.grid(row=1, column=1)

tk.Label(root, text="Preço").grid(row=2, column=0)
preco_entry = tk.Entry(root)
preco_entry.grid(row=2, column=1)

tk.Label(root, text="Conteúdo").grid(row=3, column=0)
conteudo_entry = tk.Entry(root)
conteudo_entry.grid(row=3, column=1)

tk.Button(root, text="Adicionar Curso", command=adicionar_curso).grid(row=4, column=0, columnspan=2)
tk.Button(root, text="Limpar Campos Curso", command=limpar_cursos).grid(row=4, column=2)

# Tabela para exibir os cursos
tree_cursos = ttk.Treeview(root, columns=("ID", "Título", "Descrição", "Preço", "Conteúdo"), show='headings')
tree_cursos.heading("ID", text="ID")
tree_cursos.heading("Título", text="Título")
tree_cursos.heading("Descrição", text="Descrição")
tree_cursos.heading("Preço", text="Preço")
tree_cursos.heading("Conteúdo", text="Conteúdo")
tree_cursos.grid(row=5, column=0, columnspan=3)

tk.Button(root, text="Deletar Curso", command=deletar_curso).grid(row=6, column=0, columnspan=2)

tk.Label(root, text="Buscar Curso").grid(row=7, column=0)
busca_entry = tk.Entry(root)
busca_entry.grid(row=7, column=1)
tk.Button(root, text="Buscar", command=buscar_curso).grid(row=8, column=0, columnspan=2)

# Exibir cursos no início
exibir_cursos()

# --- Seção para Usuários ---
tk.Label(root, text="Nome").grid(row=9, column=0)
nome_entry = tk.Entry(root)
nome_entry.grid(row=9, column=1)

tk.Label(root, text="Email").grid(row=10, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=10, column=1)

tk.Label(root, text="Senha").grid(row=11, column=0)
senha_entry = tk.Entry(root)
senha_entry.grid(row=11, column=1)

tk.Label(root, text="Role").grid(row=12, column=0)
role_entry = tk.Entry(root)
role_entry.grid(row=12, column=1)

tk.Button(root, text="Adicionar Usuário", command=adicionar_usuario).grid(row=13, column=0, columnspan=2)
tk.Button(root, text="Limpar Campos Usuário", command=limpar_usuarios).grid(row=13, column=2)

# Tabela para exibir os usuários
tree_usuarios = ttk.Treeview(root, columns=("ID", "Nome", "Email", "Senha", "Role"), show='headings')
tree_usuarios.heading("ID", text="ID")
tree_usuarios.heading("Nome", text="Nome")
tree_usuarios.heading("Email", text="Email")
tree_usuarios.heading("Senha", text="Senha")
tree_usuarios.heading("Role", text="Role")
tree_usuarios.grid(row=14, column=0, columnspan=3)

# Exibir usuários no início
exibir_usuarios()

root.mainloop()
