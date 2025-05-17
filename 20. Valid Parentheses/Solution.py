class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] in ['(','{', '[']:
                stack.append(s[i])
    

            if s[i] == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                    continue
                else:
                    return False

            if s[i] == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                    continue
                else:
                    return False

            if s[i] == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                    continue
                else:
                    return False
            
        
        if stack:
            return False
        else:
            return True