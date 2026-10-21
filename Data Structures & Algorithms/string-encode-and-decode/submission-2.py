class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for s in strs:
            result+=str(len(s))+'#'+s
        return result
        
    def decode(self, s: str) -> List[str]:
        decstr=[]
        i=0
        while(i<len(s)):
            j=i
            while(s[j]!='#'):
                j+=1
            lenn=int(s[i:j])
            res=s[j+1:j+1+lenn]
            decstr.append(res)
            i= j+1+lenn
        return decstr
                

        

