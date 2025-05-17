#include <iostream>
#include <cmath>

using namespace std;

void sort012Optim(vector<int> &data1);

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
    int minPrice = data1[0];
    int maxProfit = 0;

    for (int i = 0; i < data1.size(); i++)
    {
        minPrice = min(minPrice, data1[i]);
        maxProfit = max(maxProfit, data1[i] - minPrice);
    }
    return maxProfit;
}

int main()
{
    vector<int> buySellDates = {7, 1, 5, 3, 6, 4};
    cout << maxProfit(buySellDates) << endl;
    return -1;
}

void sort012Optimal(vector<int> &data1)
{
    int low = 0;
    int mid = 0;
    int high = data1.size() - 1;

    while (mid <= high)
    {
        if (data1[mid] == 0)
        {
            swap(data1[low], data1[mid]);
            low++;
            mid++;
        }
        else if (data1[mid] == 1)
        {
            mid++;
        }
        else if (data1[mid] == 2)
        {
            swap(data1[mid], data1[high]);
            high--;
        }
    }
}