#include <iostream>

int main() {
    std::cout << "I like Chapo" << '\n';
    std::cout << "Ni noma sana" << std::endl; //std::endl flushes output buffer

    int r; //Variable declaration
    r = 10; //Assigning value to variable
    int age = 20;

    int s = 6.1;
    //double (number including decimal)

    double p = 1.99;

    //Single character

    char grade = 'A'; // char can only store one character
    char dollarSign = '$';

    // boolean (true or false)
    bool on = true;
    bool off = false;

    // string (objects that represent a sequence of text)
    std::string name = "Ryan Masila";

    std::cout << r + s << '\n';
    std::cout << p << '\n';
    std::cout << grade << '\n';
    std::cout << dollarSign << '\n';
    std::cout << on << '\n';
    std::cout << off << '\n';
    std::cout << "Hello " << name << '\n';
    std::cout << "You are " << age << " years old" << '\n';
    std::cout << s;
    return 0;
}