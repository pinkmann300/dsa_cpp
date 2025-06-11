#include <iostream>
#include <cmath>

using namespace std;

long long sqrtNum2(int num);

int main()
{
    int n = 36;
    int ans = sqrtNum2(n);
    cout << "The floor of square root of " << n
         << " is: " << ans << "\n";
    return 0;
}

long long sqrtNum2(int num)
{
    long long low = 1;
    long long high = num;
    long long ans;

    while (low <= high)
    {
        long long mid = (low + high) / 2;
        long long val = (mid * mid);

        if (val <= (long long)num)
        {
            ans = mid;
            low = mid + 1;
        }
        else
        {
            high = mid - 1;
        }
    }

    return ans;
}