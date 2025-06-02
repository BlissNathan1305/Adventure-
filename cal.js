const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

let num1, num2, operator;

readline.question('Enter first number: ', (n1) => {
  num1 = parseFloat(n1);
  readline.question('Enter operator (+, -, *, /): ', (op) => {
    operator = op;
    readline.question('Enter second number: ', (n2) => {
      num2 = parseFloat(n2);

      switch (operator) {
        case "+":
          console.log(num1 + num2);
          break;
        case "-":
          console.log(num1 - num2);
          break;
        case "*":
          console.log(num1 * num2);
          break;
        case "/":
          if (num2 !== 0) {
            console.log(num1 / num2);
          } else {
            console.log("Error: Division by zero!");
          }
          break;
        default:
          console.log("Invalid operator!");
      }

      readline.close();
    });
  });
});
