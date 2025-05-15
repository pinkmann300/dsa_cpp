#include <iostream>
#include <cmath>

using namespace std;

void sort012Brute(vector<int> &data1);
void sort012CountUp(vector<int> &data1);
void sort012Optim(vector<int> &data1);
void printArray(vector<int> &data1);

int main()
{
    vector<int> data1 = {2, 2, 2, 1, 1, 1, 0, 1, 2, 2, 1, 1, 0};
    sort012Brute(data1);
    printArray(data1);
    return -1;
}

void sort012Brute(vector<int> &data1)
{
    sort(data1.begin(), data1.end());
}

void sort012CountUp(vector<int> &data1)
{
    int c1 = int c2 = int c0 = 0;
    for (int i : data1)
    {
        if (i == 0)
        {
            c0++;
        }
        else if (i == 1)
        {
            c1++;
        }
        else if (i == 2)
        {
            c2++;
        }
    }

    for (int i = 0; i < c0; i++)
    {
        data1[i] = 0;
    }
    for (int i = c0; i < c0 + c1; i++)
    {
        data1[i] = 1;
    }
    for (int i = c1; i < c1 + c2; i++)
    {
        data1[i] = 2;
    }
}

void printArray(vector<int> &data1)
{
    for (int k : data1)
    {
        cout << k << ", ";
    }

    cout << "\n";
}
