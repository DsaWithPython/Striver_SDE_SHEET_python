class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        x = 0 # missing
        y = 0 #repeatedNumber
        n = len(A)
        xor1 = A[0]
        for i in range(1,n):
            xor1=xor1^A[i]
        for i in range(1,n+1):
            xor1 = xor1^i #xor of elements and numbers from 1 to n
        
        set_bit_no = xor1 & (~(xor1 - 1)) # get rightmost set bit in set_bit_no

        for i in range(0,n):
            if A[i] & set_bit_no: #arr[i] belongs to first set
                x = x ^ A[i]
            else:
                y = y ^ A[i]# arr[i] belongs to the second set

        for i in range(1,n+1):
            if i & set_bit_no:
                x = x ^ i # i belongs to first set
            else:
                y = y ^ i # i belongs to second set
        x_count = 0
        for i in range(0,n):
            if A[i]==x:
                x_count+=1
        if x_count==0: # check if swapped
            return [y,x]
        return [x,y]
    
        
        
