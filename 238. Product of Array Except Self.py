'''238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

'''
class Solution:
    ''' Class representing a function'''    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]  # T(1) S(N)
        postfix = [1]  # T(1) S(N)

        num = 1  # T(N)
        for i in range(1,len(nums)):
            num *= nums[i-1]
            prefix.append(num)
        
        num = 1  # T(N)
        for i in range(-2,-len(nums)-1,-1):
            num *= nums[i+1]
            postfix.append(num)

        postfix1 =[postfix[i] for i in range(-1,-len(postfix)-1,-1)]  # T(N) S(N)

        output = []  # T(N)
        for i in range(len(nums)):
            output.append(prefix[i]*postfix1[i])
        return output
'''
The total time complexity is O(N)+O(N)+O(N)+O(N)=O(N).
The space complexity is O(N).
'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = i
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res