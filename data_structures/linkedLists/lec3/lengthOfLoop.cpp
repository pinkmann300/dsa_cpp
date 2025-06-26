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

int lengthOfLoop(Node *head)
{
    Node *fast = head;
    Node *slow = head;

    while (fast->next != nullptr && fast != nullptr)
    {
        fast = fast->next->next;
        slow = slow->next;

        if (slow == fast)
        {
            int count = 1;
            fast = fast->next;

            while (slow != fast)
            {
                fast = fast->next;
                count++;
            }

            return count;
        }
    }
    return 0;
}

int main()
{
    // Create a sample linked
    // list with a loop

    Node *head = new Node(1);
    Node *second = new Node(2);
    Node *third = new Node(3);
    Node *fourth = new Node(4);
    Node *fifth = new Node(5);

    // Create a loop from
    // fifth to second
    head->next = second;
    second->next = third;
    third->next = fourth;
    fourth->next = fifth;

    // This creates a loop
    fifth->next = second;

    int loopLength = lengthOfLoop(head);
    if (loopLength > 0)
    {
        cout << "Length of the loop: " << loopLength << endl;
    }
    else
    {
        cout << "No loop found in the linked list." << endl;
    }

    return 0;
}