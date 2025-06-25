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

Node *revLL(Node *head)
{
    Node *current = head;
    Node *prev = nullptr;

    while (current != nullptr)
    {
        Node *temp = current->next;
        current->next = prev;
        prev = current;
        current = temp;
    }

    return prev;
}

Node *recRevLL(Node *head, Node *result)
{
    if (head == nullptr)
    {
        return result;
    }
    else
    {
        int headVal = head->data;
        Node *newNode = new Node(headVal, result);
        return recRevLL(head->next, newNode);
    }
}

void printLinkedList(Node *head)
{
    Node *temp = head;
    while (temp != nullptr)
    {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}

int main()
{
    // Create a linked list with
    // values 1, 3, 2, and 4
    Node *head = new Node(1);
    head->next = new Node(3);
    head->next->next = new Node(2);
    head->next->next->next = new Node(4);

    // Print the original linked list
    cout << "Original Linked List: ";
    printLinkedList(head);

    // Reverse the linked list
    head = recRevLL(head, nullptr);

    // Print the reversed linked list
    cout << "Reversed Linked List: ";
    printLinkedList(head);

    return 0;
}