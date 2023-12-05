import sys
from Grafo import Grafo


def main():
    stdin = sys.argv
    stdin = stdin[1:]
    if len(stdin) != 2:
        raise Exception("Parametros invalidos")
    
    comando = stdin[0]
    parametros = stdin[1]

    