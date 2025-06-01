// This script prompts the user for their birth year and outputs their age.

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("What year were you born? ", function(birthYear) {
  const currentYear = new Date().getFullYear();
  const age = currentYear - Number(birthYear);
  console.log("You are " + age + " years old.");
  rl.close();
});
