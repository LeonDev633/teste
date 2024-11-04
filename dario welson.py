import os
os.system("cls || clear")
from dataclasses import dataclass

#defs
def limpa_tela():
    os.system("cls || clear")
    
#class
@dataclass
class Usuario:
    vendas:float
    