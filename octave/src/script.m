% Victor Cora Colombo
% RA 727356

clear all;

pkg load parallel;

n = 1e8
jobs = 32

tic();
sequencial = montecarlo_sequencial(n);
toc();
printf("Sequencial_good: %.7f\n", sequencial);

tic();
paralelo = montecarlo_paralelo_bad(n);
toc();
printf("Paralelo bad: %.7f\n", paralelo);

tic();
paralelo = montecarlo_paralelo(n, jobs);
toc();
printf("Paralelo good: %.7f\n", paralelo);