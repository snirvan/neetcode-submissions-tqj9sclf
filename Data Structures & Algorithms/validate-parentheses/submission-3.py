class Solution:
    def isValid(self, s: str) -> bool:


        # stack: ([{

        # }])


        # make hashmap of closing brackets as keys and opening brackets as values

        # if closing bracket and stack empty return false
        # if closing bracket and stack pop results in wrong item return False

        hm = {
            ")":"(", "]": "[", "}":"{"
        }
        stack = []

        for char in s:
            if char in hm.values():
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] != hm[char]:
                    return False
                
                stack.pop()
        
        return len(stack) == 0
