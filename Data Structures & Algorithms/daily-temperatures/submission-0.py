class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                output[stack[-1][0]] = index - stack[-1][0]
                stack.pop()
            stack.append((index,temp))
        return output
        




# temps: 30,38,30,36,35,40,28

# stack: 30

# output: 0 0 0 0 0 0 0 








# if stack empty add to stack
# if curr > top of stack: new arr[pop] = old[curr] - old[top]:
#     and pop
# else:
#     add to stack
