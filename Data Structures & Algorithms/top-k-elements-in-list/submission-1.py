class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        bucket=defaultdict(list)
        res=[]
        for n in nums:
            count[n]=count.get(n,0)+1
        for number,frequency in count.items():
            bucket[frequency].append(number)
        for frequency in range(len(nums),0,-1):
            for number in bucket[frequency]:
                res.append(number)
                if(len(res)==k):
                    return res 

        