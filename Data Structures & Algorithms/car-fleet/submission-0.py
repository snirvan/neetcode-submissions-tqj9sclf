class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position,speed))
        cars.sort(key = lambda x: x[0], reverse = True)
        times = [(target - p)/s for p,s in cars]
        
        stack = []
        for i in range(len(times)):
            if stack:
                peak = stack[-1]
                if times[i] <= peak:
                    continue
                else:
                    stack.append(times[i])     
            else:
                stack.append(times[i])
        
        return len(stack)
            

        
        
        
# [2.5,1.5,12]

# 4,1 


#  1,4  3,2

#  4,6
#  7,8

#  10,10


#  position[i] = position[i] + speed[i]

#  if pos1 > pos2: pos1 = pos2

#  4,1,0,7          2,2,1,1

#  6,3,1,8
#  8,5,2,9
#  10,7,3,10

 # sort to get cars in descending order
 # if p[i+1] > p[i]: p[i+1] = p[i]
 # time = round up((target - position) / speed)

#  [4,3]      [3,5,10,3] --> [10,5,3,3]
#                             [1,2,]

# if p[i] > p[i-1]: fleets[i] = fleets[i-1] + 1
#  3
#  4