#!/usr/bin/node

const arg = process.argv.slice(2);

const temp = parseInt(arg[0]);

if (typeof temp !== 'number') {
    console.log('Not a number');
} else {
    console.log('My number: '+temp);
}
