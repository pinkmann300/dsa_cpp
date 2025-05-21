// Variety-1

// Problem Statement:

// There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements.
// Without altering the relative order of positive and negative elements,
// you must return an array of alternately positive and negative values.

#include <iostream>
#include <cmath>

using namespace std;

// Function definitions:

vector<int> negPosBrute(vector<int> &data1);
vector<int> negPosOptimal(vector<int> &data1);
void printArray(vector<int> &data1);

int main()
{
    vector<int> arr1 = {1, 2, 3, -1, -2, -3};
    vector<int> rearranged_array = negPosBrute(arr1);
    printArray(rearranged_array);

    return -1;
}

vector<int> negPosBrute(vector<int> &data1)
{
    vector<int> positiveElements;
    vector<int> negativeElements;
    int length = data1.size();

    vector<int> ansArray(data1.size());

    for (int i = 0; i < length; i++)
    {
        if (data1[i] >= 0)
        {
            positiveElements.push_back(data1[i]);
        }
        else
        {
            negativeElements.push_back(data1[i]);
        }
    }

    for (int k = 0; k < positiveElements.size(); k++)
    {
        ansArray[2 * k] = positiveElements[k];

        ansArray[(2 * k) + 1] = negativeElements[k];
        printArray(ansArray);
    }

    return ansArray;
}

vector<int> negPosOptimal(vector<int> &data1)
{
    int length = data1.size(); 
    int positiveIndex = 0; 
    int negativeIndex = 1; 
    for (int i = 0; i < length; i++){

    }
}

void printArray(vector<int> &data1)
{
    for (int k : data1)
    {
        cout << k << " ,";
    }
    cout << "\n";
}