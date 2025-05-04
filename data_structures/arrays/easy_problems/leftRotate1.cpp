#include <iostream>
#include <cmath>

using namespace std;

void leftRotate1(vector<int> &data1);
void printArray(vector<int> &data1);

int main()
{
    vector<int> v3 = {1, 2, 3, 4, 5};
    leftRotate1(v3);
    printArray(v3);
}

void leftRotate1(vector<int> &data1)
{
    int length = data1.size();
    if (length > 1)
    {
        int temp = data1[0];
        for (int i = 0; i < length - 1; i++)
        {
            data1[i] = data1[i + 1];
        }
        data1[length - 1] = temp;
    }
}

void printArray(vector<int> &data1)
{
    int length = data1.size();
    for (int i = 0; i < length; i++)
    {
        cout << data1[i] << ", ";
    }
}