#include <iostream>

int main() {
    bool skip = false;
    for (char c = 'A'; c <= 'Z'; c++) {
        if (!skip) {
            std::cout << c << " ";
        }
        skip = !skip;
    }
    return 0;
}

