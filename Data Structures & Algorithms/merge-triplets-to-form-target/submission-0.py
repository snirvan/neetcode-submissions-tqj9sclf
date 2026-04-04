class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # if it has a value that is bigger than respective spot in traget: remove
        # target: [3,7,6]      triplets: [3,1,3] [2,7,5] [1,1,6] [3,7,9]

        # iterate through and add to new array but don't add any all triplets that have value bigger than respective spot
        # iterate through new array add 



        # iterate through array, if any value bigger than corresponding target value: continue
        # else add all values to respective set
        # if target value in set return True 
        # else return false

        first_target, second_target, third_target = target

        set1 = set()
        set2 = set()
        set3 = set()

        for trip in triplets:
            t1, t2, t3 = trip
            if t1 <= first_target and t2 <= second_target and t3 <= third_target:
                set1.add(t1)
                set2.add(t2)
                set3.add(t3)
        
        return first_target in set1 and second_target in set2 and third_target in set3

