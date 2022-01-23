# Notes

## 1. Find Intersection point of Y linked list

Return the nodes where the two linked lists intersect.

We will use the difference of length method. 

Take two pointers for each list and point them to the respective heads.

Iterate over the two lists by incrementing the pointers by one each time. If anytime either of the pointers becomes null, point them to the head of the other linked list and continue.

The node where the two pointers collide will be the intersection point of the two linked lists.

## 2. Detect a cycle in Linked List

Take two pointers - slow and fast.

If the linked list has a 
