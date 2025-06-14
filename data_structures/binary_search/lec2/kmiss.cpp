#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

int kmiss(vector<int> &arr, int k);
int kmiss2(vector<int> &arr, int k);

int main()
{
    vector<int> vec = {1, 2, 3, 4};

    int ans = kmiss2(vec, 4);
    cout << "The missing number is: " << ans << "\n";
    return 0;
}

int kmiss(vector<int> &arr, int k)
{

    int count = 0;
    int max_elem = *max_element(arr.begin(), arr.end());

    for (int i = 1; i <= max_elem; i++)
    {
        if (find(arr.begin(), arr.end(), i) == arr.end())
        {
            count++;
        }

        if (count == k)
        {
            return i;
        }
    }

    return (max_elem + (k - count));
}

int kmiss2(vector<int> &arr, int k)
{
    for (int i = 0; i < arr.size(); i++)
    {
        if (arr[i] <= k)
            k++; // shifting k
        else
            break;
    }
    return k;
}