% Victor Cora Colombo
% RA 727356

function r = fun(n)
    x = rand(1, n);
    y = rand(1, n);
    
    r = sum(x.^2 + y.^2 < 1.0);
endfunction