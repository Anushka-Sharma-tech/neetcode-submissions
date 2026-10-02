class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count={}
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement not in count:
                count[nums[i]]=i
            else:
                return[count[complement],i]