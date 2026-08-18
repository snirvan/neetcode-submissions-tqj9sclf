class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed), reverse= True)

        times = [0] * len(cars)
        fleets = 0
        slowest_time_ahead = 0
        for i in range(len(cars)):
            times[i] = (target - cars[i][0]) / cars[i][1]
        
        for time in times:
            if time > slowest_time_ahead:
                fleets += 1
                slowest_time_ahead = time
        
        return fleets


   
# | | | | | | | | | | | |
#  0 1 2 3 4 5 6 7 8 9 10        

# target: 10
# [10,10,4,10]