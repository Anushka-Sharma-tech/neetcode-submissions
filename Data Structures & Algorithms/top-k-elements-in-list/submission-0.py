class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        bucket=defaultdict(list)
        result=[]
        for x in nums:
            count[x]=count.get(x,0)+1
        for number,frequency in count.items():
            bucket[frequency].append(number)
        for frequency in range(len(nums),0,-1):
            for number in bucket[frequency]:
                result.append(number)
                if(len(result)==k):
                    return result
        