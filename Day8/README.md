# Notes

## N meetings in one room - Greedy

Take a list of lists - [start time, end time, meeting number].

Sort this nested list using the lambda function in python in the increasing order of ending time.

Initialise the ans variable to 1 as the first meeting will always be possible.

Take a variable limit to store the ending time oof the last meeting.

Loop from the seconf meeting to the last.

At every meeting we have two options :

if start time of current meeting is greater than limit, we can perform the meeting, so update the answer by 1.

Update limit to ending time of current meeting.

If start time is less than limit, we cannot have the meeting and we move to the next iteration.

(Create a class in python for meeting)

```
class Meeting:
  def __init__(start,end,position):
    self.start = start
    self.end = end
    self.position = position
  def compare(m1,m2):
    if m1.end<m2.end:
      return True
    elif m1.end>m2.end:
      return False
    elif m1.pos<m2.pos:
      return True
    return False
```

## Minimum number of platforms required for a railway - Greedy

Sort the arrival and depature arrays in ascending order.

Now place pointers p1 and p2 at the start of both arrays.

if arrival time of p1 is less than or equal to departure time of p2, it means a train will arrive before one departs. So we need another platform for this. We also increment p1.

If arrival time of p1 greater than the departure time at p2, this means the train is arriving after the previous departs from that platform. So, we have an extra platform. Decrement count by 1. Increment p2 by 1.

At each iteration of the loop. update maxcount with max of count and maxcount.

## Job sequencing problem - Greedy

Sort the jobs array in decreasing order of profit.

Create a res variable to store profit and initialise it to 0.

Make an array ans of size (max deadline) and set all elements to -1.

For each job, check if it can be performed on the last day.

If not, move to the previous index until that slot if empty.

If yes, assign ans of that index to the job if. Add the profit to res.

## Fractional Knapsack problem - Greedy

Pick up items with max value/weight ratio.

Sort the weight array in drcreasing order of value/weight.

For each item, there are three options.

  If weight of current item is less than  remaining weight of sack, pick the complete item.

  Add the value of the item to max_value variable and reduce the weight from the available weight for knapsack.

  If weight is greater, then get the remaiing weight by subtrating the remianing weight allowed in knapsack from the weight of the current item. 
  
  Add this value multiplied by the value to weight ratio to the final max_value variable.
  
## Find minimum number of coins - Greedy (Condition)

**ONLY** if the value of a coin is greater than sum of all previous coins with lesses values, greedy algorithm can be used for minimum number of coins.

