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

int totalLength(Node *head)
{
    int count = 0;
    while (head != nullptr)
    {
        head = head->next;
        count++;
    }

    return count;
}

int middleValue(Node *head)
{
    int totalLength2 = totalLength(head);
    int middlePos = (totalLength2 / 2) + 1;
    int counter = 0;

    while (head != nullptr)
    {
        counter++;
        if (counter == middlePos)
        {
            return head->data;
        }
        else
        {
            head = head->next;
        }
    }

    return -1;
}

int midTH(Node *head)
{
    Node *fast = head;
    Node *slow = head;

    while (fast != nullptr)
    {
        fast = fast->next->next;
        slow = slow->next;
    }

    return slow->data;
}

int main()
{
    Node *head = new Node(1);
    head->next = new Node(2);
    head->next->next = new Node(3);
    head->next->next->next = new Node(4);
    head->next->next->next->next = new Node(5);
    head->next->next->next->next->next = new Node(6);

    // Find the middle node
    int middleNode = midTH(head);

    // Display the value of the middle node
    cout << "The middle node value is: " << middleNode << endl;

    return 0;
}