class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        dict1 = {}
        count = 0
        prefix_xor = 0
        for i in A:
            prefix_xor = prefix_xor^i
            if prefix_xor == B:
                count+=1
            if prefix_xor^B in dict1.keys():
                count+= dict1[prefix_xor^B]
            if prefix_xor in dict1.keys():
                dict1[prefix_xor]+=1
            else:
                dict1[prefix_xor]=1

        return count

