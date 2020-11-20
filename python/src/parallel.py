# Aluno: Victor Cora Colombo
# RA: 727356

import sys

from mpi4py import MPI

# eh importante ter o arquivo montecarlo.py no mesmo diretorio
from montecarlo import montecarlo


def parallel(N, comm=MPI.COMM_WORLD):
    rank = comm.Get_rank()
    size = comm.Get_size()

    # usamos seed=rank para ter resultados diferentes para cada processo
    # cada processo eh responsavel por calcular o resultado para uma parcela menor do problema, de tamanho N/size
    return montecarlo(int(N/size), seed=rank)


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Quantidade incorreta de parâmetros")
        print("Uso: $ python /path/to/parallel.py N")
        sys.exit()

    # N vem como parametro do usuario
    N = int(sys.argv[1])

    # COMM_WORLD eh um comunicador que agrupa todos os processos
    comm = MPI.COMM_WORLD

    # cada processo calcula o numero de acertos individualmente
    acertos = parallel(N, comm)

    # os valores resultantes sao reunidos no processo de rank 0
    resultados = comm.gather(acertos, root=0)

    # o processo de rank 0 eh responsavel por somar os resultados e apresenta-los
    if comm.Get_rank() == 0:
        pi = (sum(resultados) / N) * 4
        print("pi = %.7f" % (pi))
