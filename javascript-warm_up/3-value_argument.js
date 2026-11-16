#!/usr/bin/node
const check = process.argv[2];
const error = 'No argument';

if (check === undefined) {
  console.log(error);
} else {
  console.log(check);
}
