#include <iostream>

int main() {
    const double PI = 3.14159;
    const int LIGHT_SPEED = 299792458;
    double radius = 7;
    double circumference = 2 * PI * radius - LIGHT_SPEED;

    std::cout << circumference << " cm";
    return 0;
}