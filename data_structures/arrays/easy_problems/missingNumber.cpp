#include <iostream>
#include <cmath>

using namespace std;

int missingNumber(vector<int> data1);

int main()
{
    return -1;
}

int missingNumber(vector<int> data1)
{
    int sumUpToN = 0;
    for (int k : data1)
    {
        sumUpToN += k;
    }

    return sumUpToN;
}