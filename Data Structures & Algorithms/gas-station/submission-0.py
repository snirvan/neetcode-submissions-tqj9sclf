class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        start = 0 
        gas_diff = 0 
        for i in range(len(gas)):
            gas_diff = gas_diff + gas[i] - cost[i]
            if gas_diff < 0:
                gas_diff = 0
                start = i + 1
        
        return start


# start = 3 
# gas_diff = -1
# i = 3

                