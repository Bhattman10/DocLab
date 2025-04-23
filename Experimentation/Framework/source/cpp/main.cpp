
#include <iostream>
#include <fstream>
#include <sstream>

int main()
{
    std::ifstream infile("text_file.txt");
    std::stringstream ss;
    ss << infile.rdbuf();

    std::cout << ss.str();
                
    return 0;
}
