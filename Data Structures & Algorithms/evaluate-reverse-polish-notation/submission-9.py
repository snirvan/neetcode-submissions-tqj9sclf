class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # pop x2,x1 and do operation x1 op x2

        stack = []
        for token in tokens:
            if token == "+":
                x2, x1 = stack.pop(), stack.pop()
                stack.append(x1 + x2)
            elif token == "-":
                x2, x1 = stack.pop(), stack.pop()
                stack.append(x1 - x2)
            elif token == "*":
                x2, x1 = stack.pop(), stack.pop()
                stack.append(x1 * x2)
            elif token == "/":
                x2, x1 = stack.pop(), stack.pop()
                stack.append(int(x1 / x2))
            else:
                stack.append(int(token))

        
        return stack[-1]