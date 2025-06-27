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

Node *oddEven(Node *head)
{
    Node *odd = new Node(-1);
    Node *even = new Node(-1);

    Node *tempo = odd;
    Node *tempe = even;

    Node *temp = head;

    while (temp != nullptr)
    {
        if (temp->data % 2 == 1)
        {
            tempo->next = new Node(temp->data);
            tempo = tempo->next;
        }
        else
        {
            tempe->next = new Node(temp->data);
            tempe = tempe->next;
        }

        temp = temp->next;
    }

    tempe->next = odd->next;
    return even->next;
}

void printLL(Node *head)
{
    while (head != nullptr)
    {
        cout << head->data << " --> ";
        head = head->next;
    }
}

int main()
{

    Node *head = new Node(1);
    head->next = new Node(2);
    head->next->next = new Node(3);
    head->next->next->next = new Node(4);
    cout << "Original list " << endl;
    printLL(head);
    cout << "\n";

    Node *segD = oddEven(head);
    printLL(segD);
    return 0;
}