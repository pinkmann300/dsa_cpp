#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int x = 15;
    cout << "The value of x at " << &x << " is " << x << endl;
    x++;
    cout << "The value of x at " << &x << " is " << x << endl;

    // The address of the variable x does not change but the value
    // of the variable has been incremented at the same memory location.

    return 0;
}