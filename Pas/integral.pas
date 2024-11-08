program root_and_integral;

const eps1 = 0.0001;
      eps2 = 0.0001;
      
type 
{$F+}
     TF = function (x: real): real;
     
var x, x12, x23, x13, a, b: real;
    mode: integer;
    
{$F+}
function f1(x: real): real; begin f1 := exp(-x) + 3 end;
function f2(x: real): real; begin f2 := 2*x - 2 end;
function f3(x: real): real; begin f3 := 1 / x end;

function f_test(x: real): real; begin f_test := x end;
function g_test(x: real): real; begin g_test := x * x end;

function root(f, g: TF; a, b: real): real; //Точка пересечения функций f и g
var c: real;
begin
  if b - a < eps1 then
    root := (a + b) / 2
  else
  begin
    c := (a + b) / 2;
    if (f(a) - g(a))*(f(c) - g(c)) <= 0 then
      root := root(f, g, a, c)
    else
      root := root(f, g, c, b)
  end
end;

function integral(f: TF; a, b: real): real; //Площаль под графиком функции f
var I1, I2, S, x, dx: real;
begin
  S := 0.5*f(a) + 0.5*f(b);
  dx := (b - a) / 4;
  x := a + dx;
  while x < b do
  begin
    S := S + f(x);
    x := x + dx
  end;
  I2 := S * dx;
  repeat
    I1 := I2;
    dx := dx / 2;
    x := a + dx;
    while x < b do
    begin
      S := S + f(x);
      x := x + 2 * dx
    end;
    I2 := S * dx;
  until abs(I2 - I1) / 3 < eps2;
  integral := I2;
end;

begin
  write('Выберете режим программы (0 - тестовый, 1 - основной): ');
  readln(mode);
  if mode = 1 then
  begin
    x12 := root(f1, f2, 2, 3);
    x23 := root(f2, f3, 1, 2);
    x13 := root(f1, f3, 0, 1);
    writeln('Точки пересечения: ', x12 : 5 : 3, ', ', x23 : 5 : 3, ', ', x13 : 5 : 3);
    writeln('Площадь криволинейного треугольника: ', integral(f1, x13, x12) - integral(f2, x23, x12) - integral(f3, x13, x23) : 5 : 3)
  end
  else
  begin
    write('Выберите тестируемую функцию (0 - root, 1 - integral): ');
    readln(mode);
    if mode = 0 then
    begin
      write('Введите отрезок: ');
      readln(a, b);
      writeln('', root(f_test, g_test, a, b))
    end
    else
    begin
      write('Введите отрезок: ');
      readln(a, b);
      writeln('', integral(g_test, a, b))
    end
  end
end.