#include <iostream>
#include <vector>

// typedef std::vector<std::pair<std::string, int>> pairlist_t;
typedef std::string text_t;
// typedef int number_t;

using number_t = int;

int main() {
    using std::cout;
    text_t text = "Ryan Masila";
    number_t num = 5;

    cout << text << '\n';
    cout << num << '\n';
    
    return 0;
}