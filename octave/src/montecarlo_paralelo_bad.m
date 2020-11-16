% Victor Cora Colombo
% RA 727356

function pi = montecarlo_paralelo_bad(n)
  x = rand(1, n);
  y = rand(1, n);
  
  fun = @(x, y) x.^2 + y.^2 < 1.0;
  
  respostas_parciais = pararrayfun(nproc, fun, x, y, "Vectorized", true, "ChunksPerProc", 8);
  
  pi = 4 * (sum(respostas_parciais) / n);
endfunction
