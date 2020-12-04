// Simple init function
// Any function is object
function myFunction() {
    var localValue = null;
}

var fac = function(n) {return n < 2 ? 1 : n * fac(n - 1);}

console.log(fac(3));

// Anonimus function
var a = new (function() {})
// Lambda / Array functions
var b = new (() => {});
const getFirst = array => array[0];
// стрелочные функции не имеют собственного контекста выполнения

const test = {
  name: 'test object',
  createAnonFunction: function() {
    return function() {
      console.log(this.name);
      console.log(arguments);
    };
  },

  createArrowFunction: function() {
    return () => {
      console.log(this.name);
      console.log(arguments);
    };
  }
};

const anon = test.createAnonFunction('hello', 'world');
const arrow = test.createArrowFunction('hello', 'world');

anon();
//undefined
//{}

arrow();
test object
{ '0': 'hello', '1': 'world' }
