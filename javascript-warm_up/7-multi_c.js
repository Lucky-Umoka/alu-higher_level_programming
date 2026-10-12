#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else if (x > 0) {
  let output = '';
  for (let i = 0; i < x; i++) {
    output += 'C is fun\n';
  }
  console.log(output.trimEnd());
}
