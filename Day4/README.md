# Short Notes

## 1. Two Sum 

Store all array elements in a dictionary in one for loop. Have another for loop where for each element, check if target-element is present in hashmap. O(n) soln.

## 2. Four Sum

One possible approach is to sort the array first, then use three pointers and binary search to find the fourth number. The time complexity for this will be big O of n log n and n cubed log n for the three pointer for the first three elements and binary search for the final element.

To reduce time complexity, we can optimize this approach. First, use two pointers. Once you subtract the sum of these two from the target, we can use a left and right pointer on the remaining array to get the required sum. 

## 3. Longest consecutive sequence

Lets store all elements in a dictionary in one loop. 

Next, we can run another for loop and have a simple check for each number. If it is the starting number of the consecutive sequence, then the dictionary will not contain x-1. If x is the starting number of the consecutive sequence, we will keep searching for the numbers y = x+1, x+2, x+3,and stop at the first y which is not present in the dictionary.

## 4. Largest subarray with zero sum

Use the concept of prefix sum for solving. Have a max length variable to store the max length of subarray with sum 0. 

Traverse the array and store the current sum. Have a dictionary for sum values and their indices observed till now. If sum value exists in dictionary, that means from that index to the current index, the sum was 0. So update max length.

If sum does not exists, add the sum and the index where it was found to the dictionary.

After traversing the entire array our max variable has the length of longest substring having sum equal to zero, so return max.

## 5. Count number of subarrays with given xor K

Have a variable for current_prefix_xor, counter and dictionary for unique xor values we have come across while traversing and their respective frequencies.

If current prefix xor is equal to K, we increment the counter. If for any index we find that current prefix xor ^ K is present dictionary, we increment the counter by dict[curr_prefix_xor^K].

## 6. Longest substring without repeat

We will take a dictionary to take the last occurence of any character. While going through a string if we encounter any repeating charater, we update the max length and start a fresh string from the index right after the one where the repeating charatecter last occured.
