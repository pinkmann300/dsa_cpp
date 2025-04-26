#include <iostream>
#include <cmath>

using namespace std;

bool isSorted(vector<int> &x);

int main()
{
    vector<int> data1 = {1, 2, 3, 4, 392, 292, 29};
    bool sorted = isSorted(data1);
    cout << "Is data 1 sorted ?  " << (sorted ? "Yes !" : "No :(") << endl;
    return 0;
}

bool isSorted(vector<int> &x)
{
    bool sorted = true;
    int length = x.size();

    for (int i = 0; i < length - 2; i++)
    {
        if (x[i] < x[i + 1])
        {
            sorted = sorted && true;
        }
        else
        {
            sorted = sorted && false;
            break;
        }
    }

    return sorted;
}