class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for c in strs:
            s+=str(len(c))+'#'+c
        return s

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while(i!=len(s)):
            k=""
            j=i
            while(s[j]!='#'):
                j+=1
            lengthh=int(s[i:j])
            k=s[j+1:j+1+lengthh]
            res.append(k)
            i=j+1+lengthh
        return res
            
