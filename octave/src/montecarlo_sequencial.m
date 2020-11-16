% Victor Cora Colombo
% RA 727356

function pi = montecarlo_sequencial(n)
  x = rand(1, n);
  y = rand(1, n);
  
  % .^2 significa elevar cada elemento do vetor ao quadrado separadamente, tambem conhecido como element-wise
  % x.^2 + y.^2 < 1.0 gera um vetor de tamanho N em que uma entrada vale 1 se esta dentro da circunferencia, e 0 caso contrario
  % sum() retorna a soma de todos os elementos do vetor
  acertos = sum(x.^2 + y.^2 < 1.0); 
  
  pi = 4 * (acertos / n);
endfunction
