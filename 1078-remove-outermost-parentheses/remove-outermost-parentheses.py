class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        depth = 0  # keeps track of balance
        
        for ch in s:
            if ch == '(':
                if depth > 0:   # not outermost
                    result.append(ch)
                depth += 1
            else:  # ch == ')'
                depth -= 1
                if depth > 0:   # not outermost
                    result.append(ch)
        
        return ''.join(result)
