# Implementação paralela do método de Monte Carlo

**This work is part of the High Performance Computer Architecture class at the Federal University of São Carlos, Brazil. Thus, it was done in Portuguese.**

## O método de Monte Carlo para a aproximação do valor de Pi

O método de Monte Carlo para a aproximação do valor de Pi consiste em colocar uma circunferência de raio 1 inscrita num quadrado. A ideia então é sortear uma grande quantidade N de pontos dentro do quadrado, de forma que se o ponto cair dentro da circunferência, é considerado um acerto. O valor aproximado de Pi então é dado por:

![equation](https://latex.codecogs.com/gif.latex?%5Cpi%20%5Csimeq%204%20%5Ccdot%20%5Cfrac%7Bacertos%7D%7BN%7D)

A derivação completa do método pode ser vista em um dos relatórios escritos para o trabalho.

## Implementação sequencial e paralela

As implementações completas em Octave e Python estão presentes nos respectivos diretórios.

- Python: [Códigos](python/src) | [Relatório](python/relatorio.pdf) | [Vídeo comentando o relatório](python/video.mp4)
- Octave: [Códigos](octave/src) | [Relatório](octave/relatorio.pdf) | [Vídeo comentando o relatório](octave/video.mp4)
