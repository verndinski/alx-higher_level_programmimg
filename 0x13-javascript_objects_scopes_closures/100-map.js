#!/usr/bin/node

// Import the array from 100-data.js
const list = require('./100-data').list;

// Compute a new array with each value multiplied by its index
const newList = list.map((value, index) => value * index);

// Print both the initial list and the new list
console.log('Initial list:', list);
console.log('New list:', newList);
