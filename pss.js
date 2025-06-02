const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

const correctPassword = "mysecretpassword";

readline.question('Enter your password: ', (userPassword) => {
  if (userPassword === correctPassword) {
    console.log("Login successful!");
  } else {
    console.log("Incorrect password. Please try again.");
  }
  readline.close();
});
