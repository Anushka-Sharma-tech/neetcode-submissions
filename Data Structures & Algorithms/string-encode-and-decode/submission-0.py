class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for st in strs:
            s+=str(len(st))+'#'+st
        return s
           
    def decode(self, s: str) -> List[str]:
        ls=[]
        i=0
        while i<len(s):
            j=s.find('#',i)
            length=int(s[i:j])
            ls.append(s[j+1:j+1+length])
            i=j+1+length
        return ls
        
