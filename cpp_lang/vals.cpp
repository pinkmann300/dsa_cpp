#include <iostream>
#include <cmath>

using namespace std;

void swapNum(int a, int b)
{
    int temp = a;
    a = b;
    b = temp;
}

void swapNumRef(int &a, int &b)
{
    int temp = a;
    a = b;
    b = temp;
}

int main()
{
    int x = 15;
    int y = 17;
    cout << "The value of x at " << &x << " is " << x << endl;
    x++;
    cout << "The value of x at " << &x << " is " << x << endl;

    // swapNum(x, y); - Does not have an impact on the values of the variables
    // because the arguments are passed by value and not by reference.

    swapNumRef(x, y);

    cout << "The value of x is : " << x << endl;
    cout << "The value of y is : " << y << endl;

    // The address of the variable x does not change but the value
    // of the variable has been incremented at the same memory location.

    // The &x gives you the address of the x variable in the memory.

    return 0;
}