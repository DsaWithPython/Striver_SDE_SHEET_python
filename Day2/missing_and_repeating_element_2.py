class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        f_sum = sum(A) #false sum
        actual_sum = 0
        actual_sum_squares = 0
        f_sum_square = 0 #false sum squares
        for i in range(1,n+1):
            actual_sum+= i
            actual_sum_squares+=i*i
            f_sum_square += A[i-1]*A[i-1]
        A =  (f_sum -  actual_sum -((f_sum_square-actual_sum_squares)//(f_sum -  actual_sum)))/2
        B = -(f_sum -  actual_sum)+A
        
        return [int(-B),int(-A)]
        
        
