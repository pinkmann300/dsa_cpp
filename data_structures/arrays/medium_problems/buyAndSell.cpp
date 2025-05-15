#include <iostream>
#include <cmath>

using namespace std;

int maxProfitBrute(vector<int> &data1)
{
    int maxProfit = 0;
    int length = data1.size();

    for (int i = 0; i < length - 1; i++)
    {
        int buy = data1[i];
        for (int j = i + 1; j < length - 1; j++)
        {
            int sell = data1[j];
            if ((sell - buy) > maxProfit)
            {
                maxProfit = sell - buy;
            }
        }
    }

    return maxProfit;
}



 int maxProfit(vector<int> &data1)
 {
 }

int main()
{
    vector<int> buySellDates = {7, 1, 5, 3, 6, 4};
    cout << maxProfitBrute(buySellDates) << endl;
    cout << INT_MAX << endl;
    return -1;
}