# Aluno: Victor Cora Colombo
# RA: 727356

import numpy as np


def montecarlo(N, seed=1234):
    np.random.seed(seed=seed)

    acertos = 0

    for i in range(N):
        # gera o ponto (x, y)
        x = np.random.random_sample()
        y = np.random.random_sample()

        # checa se (x, y) esta dentro da circunferencia
        if (x**2 + y**2 < 1):
            acertos += 1

    return acertos
