program tree_alph; // Выводит введенные слова в алфавитном порядке

type 
  w = array[1..6] of char; // Слово длиной не более 6 символов
  tree = ^node;
  node = record
    klvo: integer; // Количество вхождений
    el: w;         // Слово
    left, right: tree;
  end;

var 
  T: tree;
  cur: w; // Текущее слово
  nn: integer; // Длина текущего слова
  flag: boolean;

function ddcur(var cur, pred: w): boolean; // Проверка, равны ли два слова
var 
  i: integer;
begin
  ddcur := true;
  for i := 1 to nn do
    if cur[i] <> pred[i] then
    begin
      ddcur := false;
      exit;
    end;
end;

procedure get(var cur: w); // Считывает очередное слово
var
  ch: char;
  i, n: integer;
begin
  n := 1;
  read(ch);
  
  // Пропускаем пробелы и запятые перед началом слова
  while (ch = ' ') or (ch = ',') do
    read(ch);
  
  while (ch <> '.') and (ch <> ',') and (ch <> ' ') do
  begin
    cur[n] := ch;
    read(ch);
    n := n + 1;
  end;
  
  nn := n - 1; // Устанавливаем реальную длину слова
  for i := nn + 1 to 6 do
    cur[i] := ' '; // Заполняем оставшиеся элементы пробелами
end;

function alph(var cur, pred: w): boolean; // Возвращает true, если новое слово раньше по алфавиту
var 
  i: integer;
begin
  alph := false;
  for i := 1 to nn do
    if cur[i] < pred[i] then
    begin
      alph := true;
      exit;
    end
    else if cur[i] > pred[i] then
      exit;
end;

procedure add(var T: tree; var cur: w); // Добавляет слово в дерево
var 
  i: integer;
begin
  if T = nil then
  begin
    new(T);
    for i := 1 to 6 do
      T^.el[i] := cur[i];
    T^.left := nil;
    T^.right := nil;
    T^.klvo := 1;
  end
  else if ddcur(cur, T^.el) then 
    T^.klvo := T^.klvo + 1 // Увеличиваем счетчик, если слово уже есть
  else if alph(cur, T^.el) then
    add(T^.left, cur)
  else
    add(T^.right, cur);
end;

procedure print(var T: tree); // Печатает дерево
var 
  i: integer;
begin
  if T <> nil then
  begin
    print(T^.left);
    for i := 1 to 6 do
      if T^.el[i] <> ' ' then
        write(T^.el[i]);
    write(' ', '(', T^.klvo, ')');
    writeln;
    print(T^.right);
    dispose(T);
  end;
end;

function proverca(var cur: w; nn: integer): boolean; // Проверка корректности ввода
var 
  i: integer;
  flag: boolean;
begin
  flag := true;
  if nn > 6 then
    flag := false // Если длина больше 6, сразу ошибка
  else
    for i := 1 to nn do
      if not (cur[i] in ['A'..'Z']) then // Проверяем, что все символы в слове - латинские заглавные буквы
        flag := false;
  proverca := flag;
end;

begin
  flag := true;
  T := nil;
  while not eoln do
  begin
    get(cur);
    if proverca(cur, nn) then 
      add(T, cur)
    else 
      flag := false;
  end;

  writeln;
  if flag then 
  begin
    writeln('Полученная последовательность:');
    print(T);
  end
  else
    writeln('Ошибка ввода');
end.
