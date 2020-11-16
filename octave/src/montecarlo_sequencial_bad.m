% Victor Cora Colombo
% RA 727356

function pi = montecarlo_sequencial_bad(n)
  acertos = 0;
  for i = 1:n
    x = rand(1); % gera um número aleatório entre 0 e 1
    y = rand(1); % gera um número aleatório entre 0 e 1
    if (x^2 + y^2 < 1) % verifica se o ponto (x,y) está dentro da circunferência
      acertos = acertos + 1;
    endif
  endfor
  
  pi = 4 * (acertos / n);
endfunction
