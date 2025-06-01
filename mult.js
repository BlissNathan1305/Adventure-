function multiplicationTable(number, limit = 10) {
    console.log(`Multiplication Table of ${number}:`);
    for (let i = 1; i <= limit; i++) {
        console.log(`${number} x ${i} = ${number * i}`);
    }
}

// Example usage:
let number = 5;
multiplicationTable(number);
