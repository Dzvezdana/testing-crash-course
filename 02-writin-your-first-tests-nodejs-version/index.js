// get the first command line argument
const number = parseInt(process.argv.slice(2)[0]);

const getDigits = number => Array.from(String(number)).map(c => parseInt(c))

const getSquaredDigitsSum = n =>
  getDigits(n)
    .map(n => n ** 2)
    .reduce((a, b) => a + b, 0)

const isHappy = n => {
  const _isHappy = ([n, ...previousSteps]) =>
    previousSteps.includes(n)
      ? n === 1
      : _isHappy([getSquaredDigitsSum(n), n, ...previousSteps])
  return _isHappy([n])
}

const nextHappyNumber = (n, first = true) => ((!first && isHappy(n)) ? n : nextHappyNumber(n + 1, false))

const hasPi = number => {
  return /314/.test(String(number));
}

const isDivisibleBy7 = number => {
  return Number(number) % 7 === 0;
}

const isPrime = number => {
  let start = 2;
  const limit = Math.sqrt(number);
  while (start <= limit) {
    if (number % start++ < 1) return false;
  }
  return number > 1;
}

const isSpecialNumber = number => {
  return isHappy(number) || isDivisibleBy7(number) || hasPi(number) || isPrime(number);
}

if (number) {
  console.log("getDigits --> ", getDigits(number))
  console.log("getSquaredDigitsSum --> ", getSquaredDigitsSum(number))
  console.log("isHappy --> ", isHappy(number))
  console.log("nextHappyNumber --> ", nextHappyNumber(number))
  console.log("isSpecialNumber --> ", isSpecialNumber(number))
  console.log("hasPi --> ", hasPi(number))
  console.log("isDivisibleBy7 --> ", isDivisibleBy7(number))
  console.log("isPrime --> ", isPrime(number))
}


module.exports = {
  getDigits,
  getSquaredDigitsSum,
  isHappy,
  nextHappyNumber,
  isSpecialNumber,
  hasPi,
  isDivisibleBy7,
  isPrime,
};
