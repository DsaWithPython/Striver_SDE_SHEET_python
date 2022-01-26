# Notes

## 1. Rotate a Linked List

k = K % n for k > N

Connect the last node to the first node to convert to circular linked list.

Loop though the LL and cut the link of the last node. 

Start a node of k%n.

## 2. Clone a Linked List with random and next pointer

## 3. 3 sum

Sort the array.

Use a i pointer.

Then use two sum approch to check if sum of three numbers equals 0.

If sum<0, increment left pointer.

Else, move the right pointer to the left to reduce the sum.

## 4. Trapping rainwater

Take a left and right pointer.

Initialize leftMax and rightMax.

If height[l] less than equal to height[r] and if leftMax is less height[l],update leftMax to height[l]. Else add leftMax minus height[l] to the final answer and move the left pointer to the right.  

If height[r] is greater than rightMax, update rightMax to height[r].

Else add rightMax-height[r] to final ans and move r to left.

Repeat till l and r crosses each other.

## 5. Remove Duplicate from Sorted array

Take two pointer's i and j. 

Take a variable i as 0.

Create an loop j from 1 to n.

if arr[j]!=arr[i], increase i and update arr[i]==arr[j]

After the loop ends, return i+1,that is the size of the unique elements.

## 5. Max consecutive ones
