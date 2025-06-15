#include <iostream>
#include <cmath>

using namespace std;

// Problem Statement: You have been given a 2-D array 'mat' of size 'N x M' where 'N' and 'M' denote the number of rows and columns, respectively.
// The elements of each row are sorted in non-decreasing order. Moreover, the first element of a row is greater than the last element of the previous row (if it exists).
// You are given an integer ‘target’, and your task is to find if it exists in the given 'mat' or not.

int search2DMat(vector<vector<int>> &mat, int m);

int main()
{
    vector<vector<int>> matrix = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};
    search2DMat(matrix, 14) == true ? cout << "true\n" : cout << "false\n";
    return 0;
}

int search2DMat(vector<vector<int>> &mat, int m)
{

    int rowIndex = -1;
    bool found = false;

    for (int i = 0; i < mat.size(); i++)
    {
        int low = mat[i][0];
        int high = mat[i][mat[i].size() - 1];

        if ((low <= m) && (high >= m))
        {
            rowIndex = i;
            break;
        }
    }

    if (rowIndex == -1)
    {
        return false;
    }

    int lower = 0;
    int higher = mat[rowIndex].size() - 1;

    while (lower <= higher)
    {
        int mid = (lower + higher) / 2;
        if (mat[rowIndex][mid] == m)
        {

            found = true;
            break;
        }
        else if (mat[rowIndex][mid] > m)
        {
            higher = mid - 1;
        }
        else
        {
            lower = mid + 1;
        }
    }

    return found;
}