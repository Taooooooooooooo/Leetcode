

# double for loop. brute force.O(n^2)

class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    print([i, j])


nums = [2, 7, 11, 15]
target = 9
Solution.twoSum(nums, target)

nums = [3, 2, 4]
target = 6
Solution.twoSum(nums, target)


# dictionary storage. O(n)
class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            if target - num not in seen:
                seen[num] = i
            else:
                return [seen[target-num], i]
