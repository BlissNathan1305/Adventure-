function generatePassword(length = 12) {
  const uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  const lowercase = 'abcdefghijklmnopqrstuvwxyz';
  const numbers = '0123456789';
  const specialChars = '!@#$%^&*()_+~`|}{[]:;?><,./-=';
  const allChars = uppercase + lowercase + numbers + specialChars;

  let password = [
    getRandomChar(uppercase),
    getRandomChar(lowercase),
    getRandomChar(numbers),
    getRandomChar(specialChars)
  ];

  for (let i = 4; i < length; i++) {
    password.push(getRandomChar(allChars));
  }

  // Shuffle the password array
  password = shuffleArray(password);

  return password.join('');
}

function getRandomChar(chars) {
  return chars.charAt(Math.floor(Math.random() * chars.length));
}

function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
}

console.log(generatePassword());
