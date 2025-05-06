#include <iostream>
#include <cmath>

using namespace std;

void moveZeros(vector<int> &data1);
void printArray(vector<int> &data1);

int main()
{
    vector<int> v3 = {1, 0, 2, 3, 2, 0, 0, 4, 5, 1};
    moveZeros(v3);
    printArray(v3);
    return 0;
}

void moveZeros(vector<int> &data1)
{

    int i = -1; // Position of the very first occurence of zero in the vector.
    int length = data1.size();

    for (int k = 0; k < length; k++)
    {
        if (data1[k] == 0)
        {
            i = k;
            break;
        }
    }

    if (i != -1)
    {
        for (int j = i + 1; j < length; j++)
        {
            if (data1[j] != 0)
            {
                swap(data1[i], data1[j]);
                i++;
            }
        }
    }
}

void printArray(vector<int> &data1)
{
    for (int num : data1)
    {
        cout << num << ", "; 
    }
}