#include <iostream>
#include <cmath>

using namespace std;

// Problem Statement: You are given an array of integers 'arr' and an integer i.e. a threshold value 'limit'.
// Your task is to find the smallest positive integer divisor, such that upon dividing all the elements of the given array by it,
// the sum of the division's result is less than or equal to the given threshold value.

// Example 1:
// Input Format: N = 5, arr[] = {1,2,3,4,5}, limit = 8
// Result: 3
// Explanation: We can get a sum of 15(1 + 2 + 3 + 4 + 5) if we choose 1 as a divisor.
// The sum is 9(1 + 1 + 2 + 2 + 3)  if we choose 2 as a divisor. Upon dividing all the elements of the array by 3, we get 1,1,1,2,2 respectively. Now, their sum is equal to 7 <= 8 i.e. the threshold value. So, 3 is the minimum possible answer.

// Example 2:
// Input Format: N = 4, arr[] = {8,4,2,3}, limit = 10
// Result: 2
// Explanation: If we choose 1, we get 17 as the sum. If we choose 2, we get 9(4+2+1+2) <= 10 as the answer. So, 2 is the answer.

int smallestDivisor(vector<int> values, int limit);
int calculateLimit(vector<int> values, int divisor);

int main()
{
    vector<int> arr = {1, 2, 3, 4, 5};
    int limit = 8;
    int ans = smallestDivisor(arr, limit);
    cout << "The minimum divisor is: " << ans << "\n";
    return -1;
}

int calculateLimit(vector<int> values, int divisor)
{
    int total = 0;
    for (int i = 0; i < values.size(); i++)
    {
        total += ceil((double)(values[i]) / (double)(divisor));
    }

    return total;
}

int smallestDivisor(vector<int> values, int limits)
{
    int low = 1;
    int high = *max_element(values.begin(), values.end());
    int least = -1;

    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (calculateLimit(values, mid) <= limits)
        {
            least = mid;
            high = mid - 1;
        }
        else
        {
            low = mid + 1;
        }
    }
    return least;
}
