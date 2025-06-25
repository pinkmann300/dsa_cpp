#include <iostream>
#include <cmath>

using namespace std;

// Definition of a linked list.

class Node
{
public:
    int data;
    Node *next;

public:
    Node(int data1)
    {
        data = data1;
        next = nullptr;
    }

    Node(int data1, Node *next1)
    {
        data = data1;
        next = next1;
    }
};

int lengthOfLinkedList(Node *head)
{
    int count = 0;
    Node *temp = head;

    while (temp != nullptr)
    {
        temp = temp->next;
        count++;
    }

    return count;
}

int middleElement(Node *head)
{
    int length = lengthOfLinkedList(head);
    if (length == 0)
    {
        return 0;
    }

    Node *tail = head;
    int midPos = (length / 2) + 1;

    int tempCount = 0;

    while (tail != nullptr)
    {
        tempCount++;
        if (tempCount == midPos)
        {
            return tail->data;
        }
        tail = tail->next;
    }

    return 0;
}

int main()
{
    // Creating a sample linked list:
    Node *head = new Node(1);
    head->next = new Node(2);
    head->next->next = new Node(3);
    head->next->next->next = new Node(4);
    head->next->next->next->next = new Node(5);

    // Find the middle node
    int middleValue = middleElement(head);

    // Display the value of the middle node
    cout << "The middle node value is: " << middleValue << endl;

    return 0;
}