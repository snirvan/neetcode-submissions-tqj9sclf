class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openings = {"(":")", "{":"}","[":"]"}

        for letter in s:
            if letter in openings:
                stack.append(letter)
            else:
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                if openings[popped] != letter:
                    return False
        
        return len(stack) == 0
