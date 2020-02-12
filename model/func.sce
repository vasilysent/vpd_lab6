function y=countup(a,b)
    if a == 1 then
        b = b + 1
    end
    y = b
endfunction

function y=chooseone(mat,i,j)
    if i > size(mat)(1) then
        i = size(mat)(1)
    end
    if i < 1 then
        i = 1
    end
    y=mat(i,j)
endfunction
