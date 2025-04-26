#include <iostream>
#include <cmath>

using namespace std;

int largestElement(vector<int> &x);

int main()
{
    vector<int> data1 = {1, 2, 3, 4, 392, 292, 29};
    int max = largestElement(data1);

    cout << "The largest element in the array is : " << max << endl;
    cout << "The time complexity of this approach is O(N) and the space complexity is O(1). ";
    return 0;
}

int largestElement(vector<int> &x)
{
    int max = x.size() > 1 ? x[0] : -1;
    for (int num : x)
    {
        if (num > max)
        {
            max = num;
        }
    }

    return max;
}