const arr = [1,2,3,4];

//reducer function
console.log(arr.reduce((accumulator, currentNumber) => accumulator + currentNumber));

//for loop
let sum = 0;
for (let i = 0; i < arr.length; i++) {
    sum += arr[i];
}
console.log(sum);


//lodash lib
var lodash = require('lodash');
nextSum = lodash.sum(arr);
console.log(nextSum);