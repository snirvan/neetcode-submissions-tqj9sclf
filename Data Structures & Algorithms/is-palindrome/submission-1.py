class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        cleaned = "".join([char for char in s if char.isalnum()]).lower()
        r = len(cleaned) - 1
        while l <= r:
            if cleaned[l] != cleaned[r]:
                return False
            l += 1
            r -= 1
        
        return True
