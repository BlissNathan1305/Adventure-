function primeFactors(n) {
  const factors = [];
  let divisor = 2;
  while (n > 1) {
    if (n % divisor === 0) {
      factors.push(divisor);
      n = n / divisor;
    } else {
      divisor++;
    }
  }
  return factors;
}

for (let i = 2; i <= 40; i++) {
  console.log(`Prime factors of ${i}: ${primeFactors(i).join(', ')}`);
}
