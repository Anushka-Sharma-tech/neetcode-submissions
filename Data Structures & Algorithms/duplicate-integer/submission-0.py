class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq=defaultdict(list)
        for x in nums:
            freq[x]=freq.get(x,0)+1
        for val in freq.values():
            if(val>=2):
                return True
        return False
        