#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    unordered_map<int, string> unMap1 = {{1, "Geeks"}, {2, "For"}, {3, "Geeks"}};

    for (auto it : unMap1)
    {
        cout << it.first << " : " << it.second;
        cout << "\n";
    }
}