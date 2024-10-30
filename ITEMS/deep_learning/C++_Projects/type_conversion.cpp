#include <iostream>

int main () {
    // type conversion -> conversion of a value of one data
    //                    type to another
    //                    Implicit = automatic
    //                    Explicit = Precede value with new data type (int)
    
    double x = (int) 3.142; //Explicit

    std::cout << (char) 100 << "\n"; //Implicit

    int correct = 9;
    int questions = 10;

    double score = correct/(double) questions * 100;

    std::cout << score << "%";

    std::cout << "\n"<< x;

    }