#include <iostream>
#include <cmath>

using namespace std;

class Node
{
public:
    int data;
    Node *next;

    // Constructor
public:
    Node(int data1, Node *next1)
    {
        data = data1; // Initialize data with the provided value
        next = next1; // Initialize next with the provided
    }

    Node(int data1)
    {
        data = data1;
        next = nullptr;
    }
};

void printLL(Node *head)
{
    while (head != NULL)
    {
        cout << head->data << ", ";
        head = head->next;
    }
}

int main()
{
    vector<int> arr = {2, 5, 8, 7};
    Node *y = new Node(arr[0]);
    cout << y << '\n';       // returns the memory value
    cout << y->data << '\n'; // returns the data stored at that memory point
}
