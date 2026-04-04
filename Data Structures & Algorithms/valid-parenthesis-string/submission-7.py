class Solution:
    def checkValidString(self, s: str) -> bool:

# left: indices of (
# star: indicies of *

# iterate through 
# if (: store index in left stack
# if *: store index in right stack
# if ): if left not empty pop to match 
    # elif * not empty pop to match 

# ( may remain, try poping from star
# but if star index < left index: return false

        left = []
        star = []

        for i in range(len(s)):
            if s[i] == "(":
                left.append(i)
            elif s[i] == "*":
                star.append(i)
            elif s[i] == ")":
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False

        while left and star:
            cl = left.pop()
            cs = star.pop()

            if cs < cl:
                return False

        return len(left) == 0