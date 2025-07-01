#include <iostream>
#include <cmath>

using namespace std;

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

Node *sort012(Node *head)
{
    Node *head0 = new Node(-1);
    Node *head1 = new Node(-1);
    Node *head2 = new Node(-1);

    Node *tail0 = head0;
    Node *tail1 = head1;
    Node *tail2 = head2;

    Node *curr = head;

    while (curr != nullptr)
    {
        temp = curr;
        curr = curr->next;

        temp->next = nullptr;

        if (temp->data == 0)
        {
            tail0->next = temp;
            tail0 = temp;
        }

        if (temp->data == 1)
        {
            tail1->next = temp;
            tail1 = temp;
        }

        if (temp->data == 2)
        {
            tail2->next = temp;
            tail2 = temp;
        }
    }

    tail0->next = (head1->next != nullptr) ? head1->next : head2->next;
    tail1->next = head2->next;
    tail2->next = nullptr;
    return head0->next;
}

int main()
{
    return 0;
}