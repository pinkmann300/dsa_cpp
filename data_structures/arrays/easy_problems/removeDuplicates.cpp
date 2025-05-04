#include <iostream>
#include <cmath>

// The goal of the below program is to move the duplicates to the right of the array
// and return the count of the number of distinct elements in the array.

// Original Array : {1, 2, 3, 5, 5, 6, 7};
//                   i  j

// i and j denote two pointers from where we start. Our goal is to remove all duplicates
// through one traversal.

using namespace std;

int removeDuplicates(vector<int> &data1);

int main()
{
    vector<int> v3 = {
        1,
        2,
        2,
        2,
        3,
        4,
        4,
        392,
    };
    int k = removeDuplicates(v3);

    for (int i = 0; i < k; i++)
    {
        cout << v3[i] << " ,";
    }
}

int removeDuplicates(vector<int> &data1)
{
    int length = data1.size();
    int i = 0;
    for (int j = 1; j < length; j++)
    {
        if (data1[i] != data1[j])
        {
            i++;
            data1[i] = data1[j];
        }
    }

    return i + 1;
}