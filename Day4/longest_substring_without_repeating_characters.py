class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        n = len(s)
        st = {}
        
        max_len = 0
        while right<n:
            if s[right] in st.keys():
                st.pop(s[left])
                left+=1
            else:
                st[s[right]]=1
                max_len=max(max_len, right-left+1)
                right+=1
        return max_len
