class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett=set(nums)
        maxLen=0
        for s in sett:
            if s-1 not in sett:
                lenn=1
                while s+1 in sett:
                    lenn+=1
                    s+=1
                maxLen=max(maxLen,lenn)
        return maxLen
        

                        

        
        