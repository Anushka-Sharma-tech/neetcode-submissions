class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagroups=defaultdict(list)
        for s in strs:
            freq=[0]*26
            for c in s:
                freq[ord(c)-ord('a')]+=1
            
            anagroups[tuple(freq)].append(s)
        return list(anagroups.values())

       
   
        