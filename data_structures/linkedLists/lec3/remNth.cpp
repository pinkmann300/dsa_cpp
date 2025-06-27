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

Node *removeN(Node *head, int n)
{

    Node *fast = head;
    for (int i = 0; i < n; i++)
    {
        fast = fast->next;
    }

    Node *slow = head;

    while (fast->next != nullptr)
    {
        fast = fast->next;
        slow = slow->next;
    }

    Node *deletedNode = slow->next;
    slow->next = slow->next->next;
    delete deletedNode;

    return head;
}

void printList(Node *head)
{
    while (head != nullptr)
    {
        cout << head->data << "-->";
        head = head->next;
    }
}
int main()
{
    vector<int> arr = {1, 2, 3, 4, 5};
    int N = 3;
    Node *head = new Node(arr[0]);
    head->next = new Node(arr[1]);
    head->next->next = new Node(arr[2]);
    head->next->next->next = new Node(arr[3]);
    head->next->next->next->next = new Node(arr[4]);

    head = removeN(head, N);
    printList(head);
    return 0;
}