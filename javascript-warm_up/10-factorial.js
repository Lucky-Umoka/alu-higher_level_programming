#!/usr/bin/node
function factorial (n) {
  if (n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}
const n = parseInt(process.argv[2]);
console.log(isNaN(n) ? 1 : factorial(n));
