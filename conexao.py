import mysql.connector as mysql

def insert():

    email = e_email.get()
    nome = e_nome.get()
    telefone = e_telefone.get()

    if (email=="" or nome=="" or telefone==""):
        MessageBox.showinfo("Erro", "Todos os campos são obrigatórios")
    else:
        try:
            con = mysql.connect(host="127.0.0.1", user="root", password="root", database="cadastros")
            cursor = con.cursor()


def delete():
    if(e_rg.get() == ""):
        MessageBox.showinfo("Delete status", "RG não está inserido para delete")

    else:

      try:

        con = mysql.connect(host="localhost", user="root", password="root", database="crud_python")
        cursor = con.cursor()

def update():
    
    email = e_email.get()
    nome = e_nome.get()
    telefone = e_telefone.get();

    if (email=="" or nome=="" or telefone==""):
        MessageBox.showinfo("Update Status", "Todos os campos são Obrigatórios")
    else:

      try:

        con = mysql.connect(host="127.0.0.1", user="root", password="root", database="cadastros")
        cursor = con.cursor()