#include <iostream>
#include <vector>
#include <string>

struct Company {
    std::string name;
    std::string industry;
};

int main() {
    // List of largest companies in South Korea
    std::vector<Company> companies = {
        {"Samsung Electronics", "Electronics"},
        {"Hyundai Motor Group", "Automotive"},
        {"LG Electronics", "Electronics"},
        {"SK Group", "Conglomerate"},
        {"Kia Motors", "Automotive"},
        {"POSCO", "Steel"},
        {"Hanwha Group", "Conglomerate"},
        {"GS Group", "Conglomerate"},
        {"KT Corporation", "Telecommunications"},
        {"LG Chem", "Chemicals"}
    };

    // Print the list of companies
    std::cout << "Largest Companies in South Korea:" << std::endl;
    for (const auto& company : companies) {
        std::cout << company.name << " - " << company.industry << std::endl;
    }

    return 0;
}

