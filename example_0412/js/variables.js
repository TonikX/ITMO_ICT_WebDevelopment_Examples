/**
 * В JavaScript cуществуют три типа переменных
 */

let numberLet = 'Hello world 1';
var numberVar = 'Hello world 2';
const numberCost = 'Hello world 3';


function hoist() {
  a = 20;
  var b = 100;
  a += 2;
}

hoist();

console.log(a);
/*
Доступ как к глобальной переменной вне функции hoist()
Выводит: 20
*/
console.log(b);
/*
Как только b была назначена, она заключена в рамки области видимости функции hoist(). Что означает то, что мы не можем вывести её за рамки функции.
Вывод: ReferenceError: b is not defined
*/
