# Notes

## N meetings in one room

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

## Minimum number of platforms required for a railway

Sort the arrival and depature arrays in ascending order.

Now place pointers p1 and p2 at the start of both arrays.

if arrival time of p1 is less than or equal to departure time of p2, it means a train will arrive before one departs. So we need another platform for this. We also increment p1.

If arrival time of p1 greater than the departure time at p2, this means the train is arriving after the previous departs from that platform. So, we have an extra platform. Decrement count by 1. Increment p2 by 1.

At each iteration of the loop. update maxcount with max of count and maxcount.

## Job sequencing problem

