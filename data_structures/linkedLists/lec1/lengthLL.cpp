#include <iostream>
#include <cmath>

using namespace std;

class Node
{
public:
    int data;
    Node *next;

public:
    Node(int data1, Node *ptr)
    {
        data = data1;
        next = ptr;
    }

    Node(int data1)
    {
        data = data1;
        next = nullptr;
    }
};

int lengthOfll(Node *head)
{
    int count = 0;
    Node *temp = head;

    while (temp != NULL)
    {
        count++;
        temp = temp->next;
        }

    return count;
}

int main()
{
    vector<int> arr = {2, 5, 8, 7};

    // Create a linked list
    Node *head = new Node(arr[0]);
    head->next = new Node(arr[1]);
    head->next->next = new Node(arr[2]);
    head->next->next->next = new Node(arr[3]);

    // Print the length of the linked list
    cout << lengthOfll(head) << '\n';
    return 0;
}