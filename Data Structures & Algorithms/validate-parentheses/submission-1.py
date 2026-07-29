class Solution:
    def isValid(self, s: str) -> bool:
        map = { ')': '(', ']': '[', '}': '{'}
        stack = []
        for i in range(len(s)):
            if s[i] in map:
                if stack and map[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        return True if len(stack) == 0 else False

                    
            