# Notes

## 1. Reverse a Linked List

Take a `newHead` node and assign it to None.

We loop till head is not null. At each iteration, head moves to the next node.

Inside each iteration, assign `next` node to node.next.

Point head.next to the newHead

Assign head to the new head.

Assign next to head.

newhead  head --> next

```
head.next = newhead
newhead = head
head = next
```

## 2. Find the middle element in a linkedlist

We first take two pointers, slow and fast.

Slow moves by one step and fast movies by two steps.

So when fast reaches the last element of the linkedlist or fast moves out of the linked list, then slow reaches the middle.

This way we can get the middle element in just a single traversal.

## 3. Merge two sorted Linked Lists

We will use the merge sort method, where we make use of the fact that both lists are sorted in themselves.

 Compare the first node of both lists and assign pointer p1 to the smaller value node.

Take two pointers p1 and p2. Run a loop till either of the pointers become None.

Create a pointer resHead, to l1, which will be the head of the resultant sorted linked list.

Iterate through both lists till the value pointed by l1 is less than or equal to the value pointed by l2.

Node temp will store the last sorted node. This will help us create the link later.

Once an iteration is complete, link node pointed by temp to node pointed by l2. Then swap l1 and l2. This handles the case if  l1 ir l2 is None, then move the node pointed by temp to the next higher value node.

## 3. Remove n'th Node from back of linked list 

Take two pointers, fast and slow.

Move the fast pointer and increment a counter till it becomes n.

Next, move the slow and fast pointer simultaneously until the fast pointer reaches the end of the linked list.

Delete the node after slow by pointing slow's next to slow.next.next.

## 4. Add two numbers as linked list

Have a sum and a carry.

Loop till either of these is not 0.

sum = sum % 10

c1 = sum // 10

create a node with value sum.

## 5. Delete a given Node when a node is given

Assign the value of node.next.val to node.val

Then 
