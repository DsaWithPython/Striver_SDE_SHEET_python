# Notes

## 1. Find Intersection point of Y linked list

Return the nodes where the two linked lists intersect.

We will use the difference of length method. 

Take two pointers for each list and point them to the respective heads.

Iterate over the two lists by incrementing the pointers by one each time. If anytime either of the pointers becomes null, point them to the head of the other linked list and continue.

The node where the two pointers collide will be the intersection point of the two linked lists.

## 2. Detect a cycle in Linked List

Take two pointers - slow and fast.

If the linked list has a cycle, the fast pointer will never reach the end and will collide with slow pointer.

If slow and fast pointer collide, the linked list has a cycle.

If the fast pointer moves out of the linkedlist, cycle does not exist.

## 3. Reverse a Linked List in groups of size K

Create a node `curr` to ierate through the linked list.

Assign `curr` to head.

Interate through the linked list to get the total number of nodes n.

Have three pointers, pre, cur and nex.

Iterate through the linkedlist is groups of size k till i<k.

In each iteration, point cur to pre.next

Point nex to nex.next 

Loop for 1 to k :

Inside each iteration,  

```
pre  cur   nex                    nextGroup


```

Point cur.next to nex.next
Point nex.next to pre.next
Point pre.next to nex
Point nex to cur.next

## 4. Check if a linked list is palidrome or not

Find middle element of linked list with slow and fast pointers.

Reverse list from the element after the middle element

Iterate through both halves of the list simultaneously to check if palindrome condition stays true.

## 5. Find the starting point of a loop of a linked list

Use the slow and fast pointer method.

Slow pointer moves by one step and the fast pointer by two steps.

When fast and slow pointer collide, assign fast to the start of linked list.

Now move both slow and fast pointer by one step. 

Where they collide, that is the starting point of the linked list.\

dis covered by slow pointer : L1+L2

distance travelled by fast pointer : L1+L2+nC

when they collide - 2(L1+L2) = L1 + L2 + nC
                    L1 = nC - L2

## 6. Flattening of a linked list

Two functions Flatten and mergeTwoLL. 

Flatten we recursively flatten root.next an =d merge the next node to the current node.

We will keep recursing till the head pointer moves to null. We want to merge each list from the end.

Create a dummy node and point two pointers temp and res to the dummy node.

res will keep track of dummy code and temp pointers is to move ahead as we flatten the list.

