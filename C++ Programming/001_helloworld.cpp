#include <iostream>

// VS Code extension: C/C++ extention, Code Runner(Jun Han)

int main(){
    // standard character output
    // ; at the end of the statements

    /*
    This
    is 
    a
    multi-line
    comment
    */

    // std = standard, cout = c output, endl = end of the line, so it's start new line
    std::cout << "Hello, World!" << std::endl;
    std::cout << "My name is Fluke" << std::endl;
    std::cout << "This is my first C++ programming!" << '\n'; // this works too

    return 0; // if return 0 means no problems, if 1 there's a problem
}