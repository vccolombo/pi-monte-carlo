% Victor Cora Colombo
% RA 727356

function pi = montecarlo_paralelo(n, jobs=4)
  % repmat cria um vetor de tamanho jobs em que todas as entradas sao iguais a n/jobs. Esse valor indica o tamanho
  vetor = repmat(ceil(n/jobs), 1, jobs);
  
  % fun agora precisa estar precedido de @. Essa eh uma necessidade do pararrayfun quando fun eh uma funcao que esta em seu proprio arquivo
  respostas_parciais = pararrayfun(nproc, @fun, vetor, "Vectorized", true, "ChunksPerProc", 8);
  
  pi = 4 * (sum(respostas_parciais) / n);
endfunction
