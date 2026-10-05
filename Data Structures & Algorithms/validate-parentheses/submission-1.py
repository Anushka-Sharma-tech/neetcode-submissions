class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for s1 in s:
            if s1 in '[{(':
                stack.append(s1)
            elif s1==']':
                if not stack or stack[-1]!='[':
                    return False
                else:
                    stack.pop()
            elif s1=='}' and stack:
                if stack[-1]!='{':
                    return False
                else :
                    stack.pop()
            else:
                if not stack or stack[-1]!='(':
                    return False
                else:
                    stack.pop()
        if not stack:
            return True
        else:
            return False

        