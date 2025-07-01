#include <iostream>
#include <cmath>

using namespace std;

class Node
{
public:
    int data;
    Node *next;

public:
    Node(int x)
    {
        data = x;
        next = nullptr;
    }

    Node(int x, Node *next1)
    {
        data = x;
        next = next1;
    }
};

Node *
reverseLL(Node *head)
{
    if (head == nullptr || head->next == nullptr)
    {
        return head;
    }

    Node *newHead = reverseLL(head->next);
    Node *front = head->next;
    front->next = head;
    head->next = nullptr;

    return newHead;
}

void printLL(Node *head)
{
    while (head != nullptr)
    {
        cout << head->data << "->";
        head = head->next;
    }
}

int main()
{
    Node *head = new Node(1);
    head->next = new Node(3);
    head->next->next = new Node(2);
    head->next->next->next = new Node(4);

    // Print the original linked list
    cout << "Original Linked List: ";
    printLL(head);

    // Reverse the linked list
    head = reverseLL(head);

    // Print the reversed linked list
    cout << "Reversed Linked List: ";
    printLL(head);

    return 0;
}