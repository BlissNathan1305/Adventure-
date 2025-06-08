const correctPassword = "mysecretpassword";

const userPassword = prompt("Enter your password:");

if (userPassword === correctPassword) {
  alert("Login successful!");
  // Code to proceed after successful login
} else {
  alert("Incorrect password. Please try again.");
  // Code to handle incorrect password
}
