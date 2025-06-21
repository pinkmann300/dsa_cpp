#include <iostream>
#include <cmath>

using namespace std;

class Node
{
public:
    int data;
    Node *next;

public:
    Node(int dat1, Node *next1)
    {
        data = dat1;
        next = next1;
    }

    Node(int data1)
    {
        data = data1;
        next = nullptr;
    }
};

void printLL(Node *head)
{
    while (head != NULL)
    {
        cout << head->data << ", ";
        head = head->next;
    }
}

Node *insertHead(Node *head, int data)
{
    Node *newHead = new Node(data, head);
    return newHead;
}

int main()
{
    vector<int> arr = {12, 8, 5, 7};
    Node *head = new Node(arr[0]);
    head->next = new Node(arr[1]);
    head->next->next = new Node(arr[2]);
    head->next->next->next = new Node(arr[3]);
    head = insertHead(head, 67);

    printLL(head);
    return 0;
}