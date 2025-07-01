#include <iostream>
#include <cmath>

using namespace std;

class Node
{
public:
    int data;
    Node *back;
    Node *next;

public:
    Node(int data1, Node *back1, Node *next1)
    {
        data = data1;
        back = back1;
        next = next1;
    }

    Node(int data1)
    {
        data = data1;
        back = nullptr;
        next = nullptr;
    }
};

// Definition of a linked list.

Node *deleteAll(Node *head, int data1)
{
    if (head == nullptr || (head->next == nullptr && head->data == data1))
    {
        return head;
    }

    Node *temp = head;

    while (temp != nullptr)
    {
        if (temp->data == data1)
        {
            Node *prevNode = temp->back;
            Node *nextNode = temp->next;
            Node *current = temp;
            prevNode->next = nextNode;
            delete current;
        }
    }

    return head;
}

int main()
{
    return 0;
}