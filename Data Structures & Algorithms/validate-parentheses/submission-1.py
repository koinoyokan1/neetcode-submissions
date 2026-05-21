class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for parentheses in s:
            if parentheses in ['{', '[', '(']:
                stack.append(parentheses)
            else:
                if len(stack) == 0: return False
                lastP = stack.pop()
                if [lastP, parentheses] not in [['{','}'], ['(', ')'], ['[', ']']]: return False
        
        return len(stack) == 0
