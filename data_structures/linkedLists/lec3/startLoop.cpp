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

Node *startLoop(Node *head)
{
    Node *slow = head;
    Node *fast = head;

    while (fast != nullptr && fast->next != nullptr)
    {
        fast = fast->next->next;
        slow = slow->next;

        if (slow == fast)
        {
            slow = head;
            while (slow != fast)
            {
                fast = fast->next;
                slow = slow->next;
            }

            return fast;
        }
    }

    return nullptr;
}

int main()
{
    // Create a sample linked list with a loop
    Node *node1 = new Node(1);
    Node *node2 = new Node(2);
    node1->next = node2;
    Node *node3 = new Node(3);
    node2->next = node3;
    Node *node4 = new Node(4);
    node3->next = node4;
    Node *node5 = new Node(5);
    node4->next = node5;

    // Make a loop from node5 to node2
    node5->next = node2;

    // Set the head of the linked list
    Node *head = node1;

    // Detect the loop in the linked list
    Node *loopStartNode = startLoop(head);

    if (loopStartNode)
    {
        cout << "Loop detected. Starting node of the loop is: " << loopStartNode->data << endl;
    }
    else
    {
        cout << "No loop detected in the linked list." << endl;
    }

    return 0;
}