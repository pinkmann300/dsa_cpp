#include <iostream>
#include <cmath>

using namespace std;

class Node
{
public:
    int data;
    Node *next;

public:
    Node(int x, Node *next1)
    {
        data = x;
        next = next1;
    }

    Node(int x)
    {
        data = x;
        next = nullptr;
    }
};

Node *kReverse(Node *head, int k);

Node *getKthNode(Node *head, int k)
{
    Node *temp = head;
    while (count != k && head != nullptr)
    {
        count++;
        head = head->next;
    }
    return head;
}

Node *reverseLL(Node *head)
{
    Node *prev = nullptr;
    Node *curr = head;

    while (curr != nullptr)
    {
        Node *temp = curr->next;
        curr->next = prev;
        prev = curr;
        curr = temp;
    }

    return prev;
}

int main()
{
    return 0;
}