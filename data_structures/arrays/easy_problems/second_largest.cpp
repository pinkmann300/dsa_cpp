#include <iostream>
#include <cmath>

using namespace std;

int secondLargest(vector<int> &x);

int main()
{
    vector<int> data1 = {1, 2, 3, 4, 392, 292, 29};
    int second_largest = secondLargest(data1);

    cout << "Second largest value in the array is: " << second_largest << endl;
    return 0;
}

int secondLargest(vector<int> &x)
{
    int second_max;
    int max;

    max = second_max = x[0];

    for (int num : x)
    {
        if (num > max)
        {
            second_max = max;
            max = num;
        }
        else if (num > second_max && num != max)
        {
            second_max = num;
        }
    }

    return second_max;
}