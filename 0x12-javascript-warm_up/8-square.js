#!/usr/bin/node

const arg = process.argv.slice(2);

if (isNaN(arg[0]) || arg[0] === undefined) {
  console.log('Missing size');
} else {
  for (let index = 0; index < arg[0]; index++) {
    console.log('x'.repeat(arg[0]));
  }
}
