#include <iostream>

namespace nspace {
    int x = 3;
}

namespace nspace1 {
    int x = 5;
}

int main() {
    using namespace nspace;
    using std::cout;
    using std::string;
    string text = "hello";

    cout << x << '\n';
    std::cout << nspace::x << '\n';
    std::cout << text << '\n';
    std::cout << nspace1::x;
    return 0;
}