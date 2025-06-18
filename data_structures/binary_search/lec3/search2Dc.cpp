#include <iostream>
#include <cmath>

using namespace std;

bool searchMatrix(vector<vector<int>> &a, int target);

int main()
{
    vector<vector<int>> matrix = {{1, 4, 7, 11, 15}, {2, 5, 8, 12, 19}, {3, 6, 9, 16, 22}, {10, 13, 14, 17, 24}, {18, 21, 23, 26, 30}};
    searchMatrix(matrix, 8) == true ? cout << "true\n" : cout << "false\n";
    return 0;
}

bool searchMatrix(vector<vector<int>> &a, int target)
{
    int totalRows = a.size();
    int totalColumns = a[0].size();

    int rowPointer = 0;
    int colPointer = totalColumns - 1;

    while (rowPointer < totalRows && colPointer >= 0)
    {
        if (a[rowPointer][colPointer] == target)
        {
            return true;
        }
        else if (a[rowPointer][colPointer] > target)
        {
            colPointer--;
        }
        else
        {
            rowPointer++;
        }
    }

    return false;
}