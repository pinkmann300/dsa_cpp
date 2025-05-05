#include <iostream>
#include <cmath>

using namespace std;

void leftRotateN(vector<int> &data1, int n);
void printArray(vector<int> &data1);

int main()
{
    vector<int> v3 = {1, 2, 3, 4, 5};
    leftRotateN(v3, 7);
    printArray(v3);
    return 0;
}

void leftRotateN(vector<int> &data1, int n)
{
    int meaningfulRotations = n % data1.size();
    reverse(data1.begin(), data1.end());
    reverse(data1.begin(), data1.begin() + data1.size() - meaningfulRotations);
    reverse(data1.end() - meaningfulRotations, data1.end());
}

void printArray(vector<int> &data1)
{
    int length = data1.size();
    for (int i = 0; i < length; i++)
    {
        cout << data1[i] << ",";
    }
}