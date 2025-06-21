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

bool searchElement(Node *head, int target)
{
    Node *temp = head;

    while (temp != NULL)
    {
        if (temp->data == target)
        {
            return true;
        }
        else
        {
            temp = temp->next;
        }
    }
    return false;
}

int main()
{
    Node *head = new Node(1);
    head->next = new Node(2);
    head->next->next = new Node(5);

    int val = 5; // Element to be checked for presence in the linked list

    // Call the checkifPresent function and print the result
    cout << (searchElement(head, val) ? "True" : "False") << '\n';
    return 0;
}