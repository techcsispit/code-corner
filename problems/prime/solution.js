const fs = require("fs");

function isPrime(n) {
  if (n < 2n) return false;
  if (n === 2n || n === 3n) return true;
  if (n % 2n === 0n || n % 3n === 0n) return false;
  for (let i = 5n; i * i <= n; i += 6n) {
    if (n % i === 0n || n % (i + 2n) === 0n) return false;
  }
  return true;
}

const input = fs.readFileSync(0, "utf-8").trim();
if (input.length > 0) {
  const n = BigInt(input);
  console.log(isPrime(n) ? "prime" : "not prime");
}
