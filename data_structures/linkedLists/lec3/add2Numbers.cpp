#include <iostream>

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

Node *addTwoNumbers(Node *num1, Node *num2)
{
    int carry = 0;
    Node *ans = new Node(-1);
    Node *fin = ans;

    Node *l1 = num1;
    Node *l2 = num2;
    while (l1 != nullptr && l2 != nullptr)
    {
        int totalSum = (l1->data) + (l2->data) + carry;
        int valOnList = totalSum % 10;
        carry = totalSum / 10;
        fin->next = new Node(valOnList);
        fin = fin->next;
        l1 = l1->next; 
        l2 = l2->next; 
    }

    while (l1 != nullptr)
    {
        int totalSum = (l1->data) + carry;
        int valOnList = totalSum % 10;
        carry = totalSum / 10;
        fin->next = new Node(valOnList);
        fin = fin->next;
        l1 = l1->next; 
    }

    while (l2 != nullptr)
    {
        int totalSum2 = (l2->data) + carry;
        int valOnList2 = totalSum2 % 10;
        carry = totalSum2 / 10;
        fin->next = new Node(valOnList2);
        fin = fin->next;
        l2 = l2->next;
    }

    while (carry != 0)
    {
        int totalSum3 = carry;
        int valOnList3 = totalSum3 % 10;
        carry = totalSum3 / 10;
        fin->next = new Node(valOnList3);
        fin = fin->next;
    }

    return ans->next;
}

void printList(Node *head)
{
    while (head != nullptr)
    {
        cout << head->data << " --> ";
        head = head->next;
    }
}

int main()
{
    Node *head = new Node(9);
    head->next = new Node(9);
    head->next->next = new Node(9);

    Node *head2 = new Node(9);
    head2->next = new Node(9);
    

    Node *addedSum = addTwoNumbers(head, head2);

    printList(addedSum);

    return 0;
}
