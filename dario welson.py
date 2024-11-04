def caracteristicas_produto():
    opcao_menu2=int(input("Digite uma opção correspondente ao código:"))
    if opcao_menu2 ==1:
        print("Mil")

#Menu
print("""
Código || Descrição
1-Produtos.
2-Total a pagar.
3-Sair.
""")

#começo do código
opcao_menu=int(input("Digite uma opção correspondente ao código:"))

match(opcao_menu):
    case 1:
        print("Escolha o tipo de gelado, que você quer!")
        print("""
    Código || Decrição
    1-Milkshake
    2-Sovertes
    3-Bolos de pote.
    4-Geladinhos.
    5-Picolé
              """)
        
        
            