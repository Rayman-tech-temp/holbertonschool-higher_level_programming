#!/usr/bin/node
const check = process.argv[2];
const error = 'No argument';
const detect = 'Argument found';

if (check === undefined) {
  console.log(error);
} else if (process.argv[3] !== undefined) {
  console.log('Arguments found');
} else {
  console.log(detect);
}
