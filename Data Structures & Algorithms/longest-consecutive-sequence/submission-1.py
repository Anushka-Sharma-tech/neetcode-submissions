class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s1= set(nums)
        maxLen=0
        for s in s1:
            lengthh=1
            if s-1 not in s1:
                while s+1 in s1:
                    lengthh+=1
                    s+=1
                
                maxLen=max(maxLen,lengthh)
        return maxLen

                        

        
        