#include <iostream>

int main () {
    // cout << (insertion operator)
    // cin >> (extraction operator)

        std::string name;
        int age;

        std::cout << "What is your age? ";
        std::cin >> age;
        std::cout << "What is your full name? ";
        std::getline(std::cin >> std::ws, name);// getline() allows whitespace in a string        
        std::cout << "Your name is " << name << "\n";
        std::cout << "and" << "\n";
        std::cout << "You are " << age << " years old.";
        return 0;
}