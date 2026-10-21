class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq={}
        for n in nums:
            freq[n]=freq.get(n,0)+1
        for x in freq.values():
            if(x>=2):
                return True
        return False
      
        
        