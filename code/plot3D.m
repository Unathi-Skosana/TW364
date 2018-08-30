x = linspace(0, 1, 101);
y = linspace(0, 1, 101);
[X, Y] = meshgrid(x, y);
U = 0;

for n = 1:101
    U = U + 30.00 * (1 + (-1)^n) * ((n * pi)^3  * sinh(n * pi))^(-1) * sinh(n * pi * X) .* sin(n * pi * Y);
    U = U - 4.00 * (-1 + (-1)^n) * ((n * pi)^3  * sinh(n * pi))^(-1) * sinh(n * pi * Y) .* sin(n * pi * X);
end

surf(X,Y,U);
zlabel('U_{101}(x,y)');
xlabel('x');
ylabel('y');