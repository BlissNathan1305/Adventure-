#include <iostream>
#include <iomanip>
#include <string>
#include <vector>

struct Billionaire {
    std::string name;
    double net_worth; // in billions USD
    std::string source;
    std::string nationality;
};

// Function to print the table
void printRichList(const std::vector<Billionaire>& list) {
    // Print header
    std::cout << std::left
              << std::setw(5)  << "Rank"
              << std::setw(20) << "Name"
              << std::setw(15) << "Net Worth ($B)"
              << std::setw(30) << "Source of Wealth"
              << std::setw(15) << "Nationality"
              << std::endl;
    std::cout << std::string(85, '-') << std::endl;

    // Print each billionaire
    for (size_t i = 0; i < list.size(); ++i) {
        std::cout << std::left
                  << std::setw(5)  << (i + 1)
                  << std::setw(20) << list[i].name
                  << std::setw(15) << std::fixed << std::setprecision(1) << list[i].net_worth
                  << std::setw(30) << list[i].source
                  << std::setw(15) << list[i].nationality
                  << std::endl;
    }
}

int main() {
    // Data as of June 1, 2025, based on Forbes
    std::vector<Billionaire> richest_men = {
        {"Elon Musk", 423.0, "Tesla, SpaceX, X, xAI", "United States"},
        {"Mark Zuckerberg", 229.0, "Meta (Facebook)", "United States"},
        {"Jeff Bezos", 220.0, "Amazon, Blue Origin", "United States"},
        {"Larry Ellison", 209.0, "Oracle", "United States"},
        {"Bernard Arnault", 204.0, "LVMH", "France"},
        {"Larry Page", 178.0, "Google (Alphabet)", "United States"},
        {"Sergey Brin", 167.0, "Google (Alphabet)", "United States"},
        {"Bill Gates", 166.0, "Microsoft", "United States"},
        {"Steve Ballmer", 154.0, "Microsoft, LA Clippers", "United States"},
        {"Warren Buffett", 147.0, "Berkshire Hathaway", "United States"}
    };

    std::cout << "Top 10 Richest Men in the World as of June 1, 2025\n";
    std::cout << "Source: Forbes Real-Time Billionaires List\n\n";
    printRichList(richest_men);

    return 0;
}
