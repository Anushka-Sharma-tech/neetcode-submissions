class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        S1=set(nums)
        longestLen=0
        for s in S1:
            lengthh=1
            if s-1 not in S1:
                while s+1 in S1:
                    lengthh+=1
                    s+=1
            longestLen=max(lengthh,longestLen)
        return longestLen
        