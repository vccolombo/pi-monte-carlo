# Aluno: Victor Cora Colombo
# RA: 727356

import sys

# eh importante ter o arquivo montecarlo.py no mesmo diretorio
from montecarlo import montecarlo


def sequential(N):
    acertos = montecarlo(N)
    return (acertos / N) * 4


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Quantidade incorreta de parâmetros")
        print("Uso: $ python /path/to/sequential.py N")
        sys.exit()

    # N vem como parametro do usuario
    N = int(sys.argv[1])

    pi = sequential(N)
    print("pi = %.7f" % (pi))
