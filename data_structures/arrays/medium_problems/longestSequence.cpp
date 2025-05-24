#include <iostream>
#include <cmath>
#include <vector>
#include <unordered_set>
using namespace std;

bool linearSearch(vector<int> &data1, int target);
int longestSubSequenceBrute(vector<int> &data1);
int longestSubSequenceSort(vector<int> &data1);
int longestSubSequenceOptimal(vector<int> &data1);

int main()
{
    vector<int> arr1 = {100, 101, 1, 2, 3, 4};
    int longest = longestSubSequenceOptimal(arr1);
    cout << longest << endl;
    return -1;
}

int longestSubSequenceBrute(vector<int> &data1)
{
    int longest = 0;
    int length = data1.size();
    for (int i = 0; i < length; i++)
    {

        int cnt = 1;
        int x = data1[i];

        while (linearSearch(data1, x + 1))
        {
            cnt++;
            x++;
        }

        longest = max(cnt, longest);
    }
    return longest;
}

int longestSubSequenceSort(vector<int> &data1)
{
    sort(data1.begin(), data1.end());
    int count = 1;
    int longestCount = 0;
    int length = data1.size();

    for (int i = 0; i < length - 1; i++)
    {
        if (data1[i + 1] - data1[i] == 1 || data1[i + 1] - data1[i] == 0)
        {
            count++;
            longestCount = max(count, longestCount);
        }
        else
        {
            count = 1;
        }
    }

    return longestCount;
}

int longestSubSequenceOptimal(vector<int> &data1)
{
    int longest = 1;
    unordered_set<int> newSet;

    for (int i : data1)
    {
        newSet.insert(i);
    }

    for (auto it : newSet)
    {
        if (newSet.find(it - 1) == newSet.end())
        {
            int count = 1;
            int x = it;
            while (newSet.find(x + 1) != newSet.end())
            {
                x++;
                count++;
            }
            longest = max(longest, count);
        }
    }
    return longest;
}
// Function tested fine.
bool linearSearch(vector<int> &data1, int target)
{
    bool found = false;
    for (int k : data1)
    {
        if (k == target)
        {
            found = true;
        }
    }

    return found;
}