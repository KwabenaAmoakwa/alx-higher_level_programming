#!/usr/bin/node

const arg = process.argv.slice(2);

const temp = parseInt(arg[0]);

if (!isNaN(temp)) {
  console.log('My number: ' + temp);
} else {
  console.log('Not a number');
}
