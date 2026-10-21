class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        haveISeenYouBefore={}
        for i,n in enumerate(nums):
            complement=target-n
            if complement in haveISeenYouBefore:
                return[haveISeenYouBefore[complement],i]
            else:
                haveISeenYouBefore[n]=i
        

        
              