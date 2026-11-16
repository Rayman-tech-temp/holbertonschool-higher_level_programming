#!/usr/bin/node
const phrase = 'C is fun';
const iteration = process.argv[2];

if (iteration !== undefined) {
  for (let i = 0; i < iteration; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
