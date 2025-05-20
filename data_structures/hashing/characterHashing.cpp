#include <iostream>
#include <cmath>

using namespace std;

// Function declaration.

int main()
{
    // Creating an unordered_map with integer
    // keys and string values
    unordered_map<string, string> um =
        {{"For", "Geeks"}, {"Geeks", "For"}, {"Gees", "C++"}};

    for (auto i : um)
        cout << i.first << ": " << i.second
             << endl;
    return 0;
}