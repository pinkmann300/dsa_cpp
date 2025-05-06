#include <iostream>
#include <cmath>

using namespace std;

int linearSearch(vector<int> &data1, int target);
int main()
{
    vector<int> v3 = {1, 2, 3, 4, 5, 6, 6, 7};
    int three_index = linearSearch(v3, 4);
    cout << three_index << endl;
    return 0;
}

int linearSearch(vector<int> &data1, int target)
{
    int index = -1;
    int length = data1.size();

    for (int i = 0; i < length; i++)
    {
        if (data1[i] == target)
        {
            index = i;
            break;
        }
    }

    return index;
}