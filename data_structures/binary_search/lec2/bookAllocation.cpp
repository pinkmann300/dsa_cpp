#include <iostream>
#include <cmath>
#include <algorithm>
#include <numeric>

using namespace std;

// Problem Statement: Given an array ‘arr of integer numbers, ‘ar[i]’ represents the number of pages in the ‘i-th’ book.
// There are a ‘m’ number of students, and the task is to allocate all the books to the students.
// Allocate books in such a way that:

// Each student gets at least one book.
// Each book should be allocated to only one student.
// Book allocation should be in a contiguous manner.
// You have to allocate the book to ‘m’ students such that the maximum number of pages assigned to a student is minimum.
// If the allocation of books is not possible. return -1

// Example 1:
// Input Format: n = 4, m = 2, arr[] = {12, 34, 67, 90}
// Result: 113
// Explanation: The allocation of books will be 12, 34, 67 | 90. One student will get the first 3 books and the other will get the last one.

// Example 2:
// Input Format: n = 5, m = 4, arr[] = {25, 46, 28, 49, 24}
// Result: 71
// Explanation: The allocation of books will be 25, 46 | 28 | 49 | 24.

int minimumPages(vector<int> &books, int m);
int countStudetns(vector<int> &books, int pages);

int main()
{
    vector<int> arr = {25, 46, 28, 49, 24};
    int n = 5;
    int m = 4;
    int ans = minimumPages(arr, m);
    cout << "The answer is: " << ans << "\n";
    return 0;
}

// Answer lies in the range (max(arr), sum(arr));
int countStudents(vector<int> &books, int pages)
{
    int noOfStudents = 1;
    int studentPages = 0;

    for (int i = 0; i < books.size(); i++)
    {
        if (books[i] + studentPages <= pages)
        {
            studentPages += books[i];
        }
        else
        {
            noOfStudents++;
            studentPages = books[i];
        }
    }
    return noOfStudents;
}

int minimumPages(vector<int> &books, int m)
{
    int low = *max_element(books.begin(), books.end());
    int high = accumulate(books.begin(), books.end(), 0);

    int minimumPages = -1;

    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (countStudents(books, mid) > m)
        {
            low = mid + 1;
        }
        else
        {
            minimumPages = mid;
            high = mid - 1;
        }
    }

    return minimumPages;
}
