#include <iostream>
#include <cmath>
#include <map>

using namespace std;

int majorityElementBrute(vector<int> &data1);
int majorityHashMap(vector<int> &data1);
int majorityOptimal(vector<int> &data1);

int main()
{
    vector<int> arr = {2, 2, 1, 1, 1, 2, 2};
    cout << majorityOptimal(arr) << endl;
    return -1;
}

int majorityElementBrute(vector<int> &data1)
{
    int maxElement = -1;
    for (int i = 0; i < data1.size(); i++)
    {
        int elementCount = 0;
        for (int j = 0; j < data1.size(); j++)
        {
            if (data1[i] == data1[j])
            {
                elementCount++;
            }
        }

        if (elementCount > (data1.size() / 2))
        {
            return data1[i];
        }
    }
    return maxElement;
}

int majorityHashMap(vector<int> &data1)
{
    map<int, int> map1;
    for (int i = 0; i < data1.size(); i++)
    {
        map1[data1[i]]++;
    }

    for (auto it : map1)
    {
        if (it.second > (data1.size() / 2))
        {
            return it.first;
        }
    }

    return -1;
}

int majorityOptimal(vector<int> &data1)
{
    int votes = 0;
    int candidate = -1;

    for (int i = 0; i < data1.size(); i++)
    {
        if (votes == 0)
        {
            candidate = data1[i];
            votes = 1;
        }
        else
        {
            if (data1[i] == candidate)
            {
                votes++;
            }
            else
            {
                votes--;
            }
        }
    }

    return candidate; // Based on the assumption that every array is promised to have such an element.
}