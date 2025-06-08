#include <iostream>

int main() {
  for (char letter = 'a'; letter <= 'z'; ++letter) {
    std::cout << letter;
    ++letter; // Skip the next letter
    if (letter > 'z') {
      break; // Avoid going beyond 'z'
    }
  }
  std::cout << std::endl;
  return 0;}
