// Recursion Practice

// Question 1: Sum all numbers
// Write a function called sumRange. It will take a number and return the sum of all numbers
// from 1 up to the number passed in.
// Sample: sumRange(3) returns 6, since 1 + 2 + 3 = 6.
function sumRange(n) {
  if (n === 1) return 1;
  return n + sumRange(n - 1);
}
console.log(sumRange(10));


// Question 2: Power function
// Write a function called power which takes in a base and an exponent.
// If the exponent is 0, return 1.
function power(base, exponent) {
  if (exponent === 0) return 1
  return base * power(base, exponent - 1)
}

console.log(power(2, 4));
