#include <iostream>
#include <cmath>
#include <numeric>
#include <algorithm>
#include <vector>

using namespace std;

double median(vector<int> &arr1, vector<int> &arr2);

int main()
{
    vector<int> a = {1, 4, 7, 10, 12};
    vector<int> b = {2, 3, 6, 15};
    cout << "The median of two sorted array is " << (median(a, b)) << '\n';
    return -1;
}

double median(vector<int> &a, vector<int> &b)
{
    // size of two given arrays:
    int n1 = a.size(), n2 = b.size();

    vector<int> arr3;
    // apply the merge step:
    int i = 0, j = 0;
    while (i < n1 && j < n2)
    {
        if (a[i] < b[j])
            arr3.push_back(a[i++]);
        else
            arr3.push_back(b[j++]);
    }

    // copy the left-out elements:
    while (i < n1)
        arr3.push_back(a[i++]);
    while (j < n2)
        arr3.push_back(b[j++]);

    // Find the median:
    int n = n1 + n2;
    if (n % 2 == 1)
    {
        return (double)arr3[n / 2];
    }

    double median = ((double)arr3[n / 2] + (double)arr3[(n / 2) - 1]) / 2.0;
    return median;
}