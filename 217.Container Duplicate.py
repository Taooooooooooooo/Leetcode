'''Given an integer array nums, 
return true if any value appears at least twice in the array, and 
return false if every element is distinct.
Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''
class Solution:
    def containsDuplicate(nums):
        hashset = set()  # set
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        else:
            return False 
        
''' T(n),Space(n)'''

class Solution:
    def containsDuplicate(nums):
        return len(nums) != len(set(nums))

''' T(n),Space(n)'''  
    

class Solution:
    def containsDuplicate(nums):
        nums.sort()   #  The average time complexity is O(n log n)
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True
            return False
'''T(n log n),Space(1) '''