#include <iostream>
#include <cmath>

using namespace std;

class Node
{
public:
    int data;
    Node *next;
    Node *prev;

public:
    Node(int data1)
    {
        data = data1;
        next = nullptr;
        prev = nullptr;
    }

    Node(int data1, Node *next1, Node *prev1)
    {
        data = data1;
        next = next1;
        prev = prev1;
    }
};

Node *deleteLastNode(Node *head)
{
    if (head == nullptr || head->next == nullptr)
    {
        return nullptr;
    }

    Node *tail = head;
    while (tail->next != nullptr)
    {
        tail = tail->next;
    }

    Node *newTail = tail->prev;
    newTail->next = nullptr;
    delete tail;

    return head;
}
// Class definition of a node ends here.
Node *insertAtHead(Node *head, int value)
{
    Node *newNode = new Node(value, head, nullptr);
    return newNode;
}

Node *insertAtTail(Node *head, int value)
{
    Node *newNode = new Node(value);
    if (head == nullptr)
    {
        return newNode;
    }

    Node *tail = head;
    while (tail->next != nullptr)
    {
        tail = tail->next;
    }

    tail->next = newNode;
    newNode->prev = tail;

    return head;
}

Node *convertArrToDLL(vector<int> arr1)
{
    Node *head = new Node(arr1[0]);

    Node *tail = head;

    for (int i = 1; i < arr1.size(); i++)
    {
        Node *newNode = new Node(arr1[i], nullptr, tail);
        tail->next = newNode;
        newNode->prev = tail;
        tail = tail->next;
    }

    return head;
}

Node *reverseDLL(Node *head)
{
    if (head == nullptr || head->next == nullptr)
    {
        return nullptr;
    }

    Node *prev = nullptr;
    Node *current = head;

    while (current != nullptr)
    {
        prev = current->back;
        current->back = current->next;
        current->next = prev;
        current = current->back;
    }

    return prev->back;
}

void printDll(Node *head)
{
    while (head != nullptr)
    {
        cout << head->data << " <-> ";
        head = head->next;
    }
}

int main()
{
    vector<int> arr = {12, 5, 8, 7, 4};
    Node *head = convertArrToDLL(arr);

    cout << "Doubly Linked List Initially: " << endl;
    printDll(head);

    cout << endl
         << "Doubly Linked List After Inserting at the tail with value 10: " << endl;
    // Insert a node with value 10 at the end
    head = insertAtTail(head, 10);
    head = insertAtHead(head, 10);
    head = deleteLastNode(head);
    printDll(head);

    return 0;
}