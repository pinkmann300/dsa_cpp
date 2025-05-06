#include <iostream>
#include <cmath>
#include <set>

using namespace std;

vector<int> unionFind(vector<int> &data1, vector<int> &data2);
vector<int> setApproach(vector<int> &data1, vector<int> &data2);
void printArray(vector<int> &data1); // Utility function to print an array.

int main()
{
    vector<int> v3 = {1, 2, 3, 4, 5, 6, 7};
    vector<int> v2 = {1, 2, 3, 4, 5, 6};
    // vector<int> finalResult = setApproach(v3, v2);

    vector<int> finalResult = unionFind(v3, v2);

    for (int k : finalResult)
    {
        cout << k << " ,";
    }
    return 0;
}

vector<int> setApproach(vector<int> &data1, vector<int> &data2)
{
    set<int> union1;
    for (int num : data1)
    {
        union1.insert(num);
    }

    for (int num2 : data2)
    {
        union1.insert(num2);
    }

    vector<int> union_vector(union1.begin(), union1.end());
    return union_vector;
}

vector<int> unionFind(vector<int> &data1, vector<int> &data2)
{
    // The following method uses the two pointer approach taking
    // advantage of the fact that the two arrays are sorted.

    int i = 0;
    int j = 0;

    int length1 = data1.size();
    int length2 = data2.size();

    vector<int> finalVector;

    while (i < length1 && j < length2)
    {
        if (data1[i] == data2[j])
        {
            if (finalVector.size() != 0 && finalVector.back() == data1[i])
            {
                j++;
                i++;
            }
            else
            {
                finalVector.push_back(data1[i]);
                i++;
                j++;
            }
        }
        else if (data1[i] > data2[j])
        {
            if (finalVector.size() != 0 && finalVector.back() == data2[j])
            {
                j++;
            }
            else
            {
                finalVector.push_back(data2[j]);
                j++;
            }
        }
        else if (data1[i] < data2[j])
        {
            if (finalVector.size() != 0 && finalVector.back() == data1[i])
            {
                i++;
            }
            else
            {
                finalVector.push_back(data1[i]);
                i++;
            }
        }
    }

    while (i < length1)
    {
        finalVector.push_back(data1[i]);
        i++;
    }

    while (j < length2)
    {
        finalVector.push_back(data2[j]);
        j++;
    }

    return finalVector;
}

void printArray(vector<int> &data)
{
    for (int i : data)
    {
        cout << i << " , ";
    }
    cout << "\n";
}