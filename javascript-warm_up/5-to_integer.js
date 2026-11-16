#!/usr/bin/node
const number = process.argv[2];
if (number !== undefined && !isNaN(number)) {
  console.log('My number: ' + number);
} else {
  console.log('Not a number');
}
