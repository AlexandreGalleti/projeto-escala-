import tkinter as tk
from tkinter import messagebox


current_username = "Adm"
current_password = "1234"

def check_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == current_username and password == current_password:
        messagebox.showinfo("Login", "Login bem-sucedido!")
        show_main_page()
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos!")

def show_main_page():
    login_frame.pack_forget()
    main_frame.pack(fill='both', expand=True)

    label.config(text="Olá, Mundo!")
    main_frame.pack(pady=20)
    button.pack(pady=10)
    change_user_button.pack(pady=10)
    change_pass_button.pack(pady=10)

def change_username():
    global current_username
    new_username = username_entry_new.get()
    if new_username:
        current_username = new_username
        messagebox.showinfo("Sucesso", "Nome de usuário alterado com sucesso!")
        show_main_page()
    else:
        messagebox.showerror("Erro", "O nome de usuário não pode estar vazio.")

def change_password():
    global current_password
    new_password = password_entry_new.get()
    if new_password:
        current_password = new_password
        messagebox.showinfo("Sucesso", "Senha alterada com sucesso!")
        show_main_page()
    else:
        messagebox.showerror("Erro", "A senha não pode estar vazia.")

def show_change_user_frame():
    main_frame.pack_forget()
    change_user_frame.pack(fill='both', expand=True, pady=20)

def show_change_pass_frame():
    main_frame.pack_forget()
    change_pass_frame.pack(fill='both', expand=True, pady=20)

window = tk.Tk()
window.title("Sistema de Login")
window.geometry("800x600")


login_frame = tk.Frame(window)
login_frame.pack(fill='both', expand=True, pady=20)

username_label = tk.Label(login_frame, text="Usuário:")
username_label.pack(pady=5)
username_entry = tk.Entry(login_frame)
username_entry.pack(pady=5)

password_label = tk.Label(login_frame, text="Senha:")
password_label.pack(pady=5)
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack(pady=5)

login_button = tk.Button(login_frame, text="Login", command=check_login)
login_button.pack(pady=10)


main_frame = tk.Frame(window)

label = tk.Label(main_frame, text="", font=("Helvetica", 16))
label.pack(pady=20)

button = tk.Button(main_frame, text="Clique em mim", command=lambda: label.config(text="Botão clicado!"))
button.pack(pady=10)


change_user_button = tk.Button(main_frame, text="Alterar nome de usuário", command=show_change_user_frame)
change_pass_button = tk.Button(main_frame, text="Alterar senha", command=show_change_pass_frame)


change_user_frame = tk.Frame(window)

username_label_new = tk.Label(change_user_frame, text="Novo nome de usuário:")
username_label_new.pack(pady=5)
username_entry_new = tk.Entry(change_user_frame)
username_entry_new.pack(pady=5)

confirm_user_button = tk.Button(change_user_frame, text="Confirmar", command=change_username)
confirm_user_button.pack(pady=10)

change_pass_frame = tk.Frame(window)

password_label_new = tk.Label(change_pass_frame, text="Nova senha:")
password_label_new.pack(pady=5)
password_entry_new = tk.Entry(change_pass_frame, show="*")
password_entry_new.pack(pady=5)

confirm_pass_button = tk.Button(change_pass_frame, text="Confirmar", command=change_password)
confirm_pass_button.pack(pady=10)

window.mainloop()
