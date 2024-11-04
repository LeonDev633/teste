def caracteristicas_produto():
    pass

# Menu
print("""
Código || Descrição
1 - Produtos.
2 - Tamanho do produto.
3 - Sabores.
4 - Total a pagar.
5 - Sair.
""")

# Funções para cada opção do menu
def listar_produtos():
    print("Tipos de gelado disponíveis: Sorvete, Sorbet, Gelato.")

def tamanho_produto():
    print("Tamanhos disponíveis: Pequeno, Médio, Grande.")

def listar_sabores():
    print("Sabores disponíveis: Chocolate, Baunilha, Morango, Pistache, Manga.")

def total_a_pagar():
    print("Total a pagar: R$ 20,00")  # Simulação de valor

# Início do código
opcao_menu = int(input("Digite uma opção correspondente ao código: "))

match opcao_menu:
    case 1:
        listar_produtos()
    case 2:
        tamanho_produto()
    case 3:
        listar_sabores()
    case 4:
        total_a_pagar()
    case 5:
        print("Saindo...")
    case _:
        print("Opção inválida. Por favor, tente novamente.")
