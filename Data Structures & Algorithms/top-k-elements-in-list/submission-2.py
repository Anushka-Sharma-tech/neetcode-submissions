class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nTofMapper={}
        ftoNsMapper=defaultdict(list)
        result=[]
        for n in nums:
            nTofMapper[n]=nTofMapper.get(n,0)+1
        for n,f in nTofMapper.items():
            ftoNsMapper[f].append(n)
        for f in range(len(nums),0,-1):
            for n in ftoNsMapper[f]:
                result.append(n)
                if(len(result)==k):
                    return result


        

        