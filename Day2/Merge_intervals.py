class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged_intervals = []
        if len(intervals)==0:
            return merged_intervals
        intervals = sorted(intervals)
        temp_interval = intervals[0]
        for i in intervals:
            if i[0]<=temp_interval[1]:
                temp_interval[1] = max(i[1],temp_interval[1])
            else:
                merged_intervals.append(temp_interval)
                temp_interval = i
        merged_intervals.append(temp_interval)
        return merged_intervals
        
