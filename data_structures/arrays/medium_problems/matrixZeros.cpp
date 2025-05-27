#include <iostream>
#include <cmath>

using namespace std;

void setZerosBrute(vector<vector<int>> &data1);
void printMatrix(vector<vector<int>> &data1);
void printVector(vector<int> &data1);

int main()
{
    vector<vector<int>> matrix = {{1, 1, 1}, {1, 0, 1}, {1, 1, 1}};
    printMatrix(matrix);
    return -1;
}

void printVector(vector<int> &data1)
{
    for (int i : data1)
    {
        cout << i << " ";
    }
}

void printMatrix(vector<vector<int>> &data1)
{
    for (vector<int> i : data1)
    {
        printVector(i);
        cout << "\n";
    }
}

// void setZerosBrute(vector<vector<int>> &data1){
//     for (int i )
// }