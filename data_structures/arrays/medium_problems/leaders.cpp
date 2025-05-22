#include <iostream>
#include <cmath>

using namespace std;

vector<int> leadersOfArrayBrute(vector<int> &data1);
vector<int> leadersOfArrayOptimal(vector<int> &data1);
void printArray(vector<int> &data1);

int main()
{
    vector<int> arr1 = {10, 22, 12, 3, 0, 6};
    vector<int> leaders = leadersOfArrayBrute(arr1);
    printArray(leaders);
    return -1;
}

vector<int> leadersOfArrayBrute(vector<int> &data1)
{
    int length = data1.size();
    vector<int> leaderArr;
    for (int i = 0; i < length; i++)
    {
        bool leader = true;
        for (int j = i + 1; j < length; j++)
        {
            if (data1[j] > data1[i])
            {
                leader = leader && false;
                break;
            }
        }

        if (leader)
        {
            leaderArr.push_back(data1[i]);
        }
    }

    return leaderArr;
}

void printArray(vector<int> &data1)
{
    for (int i : data1)
    {
        cout << i << ", ";
    }
    cout << "\n";
}