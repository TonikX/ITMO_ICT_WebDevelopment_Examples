var names = [ "Ernie", "Bert", "Oscar" ];

// for
for (var i = 0; i < names.length; i++) {
    console.log(names[i]);  //Print value to console
}

// Проверяет условие перед каждой итерацией.
// цикл с предусловием
// while (condition) {
// }

// Проверяет условие после каждой итерации.
// цикл с постусловием
// do {
// } while (condition)


// Map
// Метод map() создаёт новый массив с результатом вызова указанной функции для каждого элемента массива.
// Метод map не изменяет массив

var numbers = [1, 4, 9];

var roots = numbers.map(Math.sqrt);
var rootsArrow = numbers.map((element) => Math.sqrt(element))

console.log({numbers, roots, rootsArrow})


// Foreach
// Метод forEach() выполняет указанную функцию один раз для каждого элемента в массиве. Не изменяет исходный массив
const items = ['item1', 'item2', 'item3']
const copy = []

// до
for (let i = 0; i < items.length; i++) {
  copy.push(items[i])
}

// после
items.forEach(function(item){
  copy.push(item)
})

let testForEach = [];

items.forEach((item) => {
    testForEach.push(item);
})

var arr = ["Яблоко", "Апельсин", "Груша"];

arr.forEach(function(item, i, arr) {
  console.log( i + ": " + item + " (массив:" + arr + ")" );
});


// Filter 
// Создает новый массив из результатов фильтрации

var arr = [1, -1, 2, -2, 3];

var positiveArr = arr.filter((number) => {
  return number > 0;
});

// Reduce
// При первом запуске sum – исходное значение, с которого начинаются вычисления, равно нулю (второй аргумент reduce).
// Сначала анонимная функция вызывается с этим начальным значением и первым элементом массива, 
// результат запоминается и передаётся в следующий вызов, уже со вторым аргументом массива, 
// затем новое значение участвует в вычислениях с третьим аргументом и так далее.

var arr = [1, 2, 3, 4, 5]

// убрали 0 в конце
var result = arr.reduce(function(sum, current) {
  return sum + current
});




