class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for st in s:
            if st=='(' or st=='{' or st=='[':
                stack.append(st)
            elif st==']':
                if not stack or stack[-1]!='[':
                    return False
                else:
                    stack.pop()
            elif st=='}':
                if not stack or stack[-1]!='{':
                    return False
                else:
                    stack.pop()
            elif st==')':
                if not stack or stack[-1]!='(':
                    return False
                else:
                    stack.pop()
        if not stack:
            return True
        else:
            return False
            
    

        