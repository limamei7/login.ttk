import tkinter as tk
from tkinter import ttk, messagebox

# verificar as credenciais
def verificar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    # definir login e senha
    if usuario == "lima" and senha == "cu":
        messagebox.showinfo("Login", "aí vc ta demonstrando a essencia")
    else:
        messagebox.showerror("Erro", "errou tenta dnv")

# janela principal
root = tk.Tk()
root.title("Tela de Login")
root.geometry("300x250")
root.configure(bg="#000000")

# Estilo ne pae
style = ttk.Style()
style.configure("TLabel", background="#000000", foreground="blue", font=("verdana", 12))
style.configure("TEntry", font=("verdana", 12))
style.configure("TButton", font=("verdana", 12))

# widigets
label_usuario = ttk.Label(root, text="Usuário:")
label_usuario.pack(pady=(20, 5))

entry_usuario = ttk.Entry(root)
entry_usuario.pack(pady=(0, 15))

label_senha = ttk.Label(root, text="Senha:")
label_senha.pack(pady=(0, 5))

entry_senha = ttk.Entry(root, show="*")
entry_senha.pack(pady=(0, 15))

botao_login = ttk.Button(root, text="Entrar", command=verificar_login)
botao_login.pack(pady=20)

# loop da interface
root.mainloop()