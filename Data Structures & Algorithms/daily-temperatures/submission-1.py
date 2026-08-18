class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        # compare arr[index]
        # res[stack index] = curr index - stack index 
        # pop 
        # push to stack
        
        
        # stack: 5,
    

        # result = 1,4,1,2,1
        temp_len = len(temperatures)
        stack = []
        res = [0] * len(temperatures)

        for i in range(temp_len):
            if len(stack) == 0:
                stack.append(i)
            else:
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    res[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
        return res
