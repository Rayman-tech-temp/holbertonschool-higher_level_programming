#!/usr/bin/node
const check = process.argv[2];
const error = 'No argument';
const detect = 'Argument found';

if (check === undefined) {
  console.log(error);
} else {
  console.log(detect);
}
