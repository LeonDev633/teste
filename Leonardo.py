def menu():
    print("""
1-
2-
3- 
0-
""")

def cadastro():
    from Banco import Usuario
    usuario = Usuario{
        cpf = input("CPF: "),
        nome = input("NOME: "),
        sobrenome = input("SOBRENOME: "),
        senha = input("SENHA: ")
    }

def principado():
    while True:
        menu()
        while True:
            opcao = int(input(": "))
            if opcao in [1,2,3,0]:
                break
        match opcao:
            case 1:
                cadastro()             
            case 2:
                pass
            case 3:
                pass
            case 0:
                pass
            case _:
                break