#include <iostream>
#include <cmath>
#include <set>

using namespace std;

vector<int> unionFind(vector<int> &data1, vector<int> &data2);
vector<int> setApproach(vector<int> &data1, vector<int> &data2);

int main()
{
    vector<int> v3 = {1, 2, 3, 4, 5, 6, 7};
    vector<int> v2 = {1, 2, 3, 4, 5, 6};
    vector<int> finalResult = setApproach(v3, v2);

    for (int k : finalResult)
    {
        cout << k << " ,";
    }
    return 0;
}

vector<int> setApproach(vector<int> &data1, vector<int> &data2)
{
    set<int> union1;
    for (int num : data1)
    {
        union1.insert(num);
    }

    for (int num2 : data2)
    {
        union1.insert(num2);
    }

    vector<int> union_vector(union1.begin(), union1.end());
    return union_vector;
}
