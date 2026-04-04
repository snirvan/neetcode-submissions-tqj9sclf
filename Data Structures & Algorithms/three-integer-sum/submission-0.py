class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right =  len(nums) - 1
            while left < right:
                target = -1 * nums[i]
                if nums[left] + nums[right] == target:
                    res.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1

        return res

# i    j           k
# -1, -1, 0, 1, 2, 4

# sort
# loop through
# two point left and right (while j<k)
    # if less than traget j++ until nums[j] != nums[j-1]
    # if greater than target k-- until nums[k] != nums[k+1]
