#https://leetcode.com/problems/maximum-subarray/description/

from typing import List

"""
TECHNIQUE: Brute Force
PROCEDURE:
1. Create a for loop to traverse from first to last element of the array.
    This for loop represents the first element of subarray.
2. Initialize a variable curr_sum to calculate the running sum of the subarray in consideration.
3. Create a nested for loop which traverses from start of subarray to end of array. Within this loop:
    3.1 Add current element of subarray to curr_sum.
    3.2 Calculate maximum of current subarray sum (curr_sum) and maximum so far.
    3.3 Keep adding the last element of subarray (represented by nested loop) to curr_sum 
        and updating the maximum value.
TIME COMPLEXITY: O(n^2)
SPACE COMPLEXITY: O(1)
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = pow(-10,5)
        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                maximum = max(maximum, curr_sum)
        return maximum

"""
TECHNIQUE: Unoptimized DP
PROCEDURE:
1. Check if all the numbers of 
Create a for loop to traverse all elements of the array.
    This for loop represents the first element of subarray.
2. Initialize a variable curr_sum to calculate the running sum of the subarray in consideration.
3. Create a nested for loop which traverses from start of subarray to end of array. Within this loop:
    3.1 Add current element of subarray to curr_sum.
    3.2 Calculate maximum of current subarray sum (curr_sum) and maximum so far.
    3.3 Keep adding the last element of subarray (represented by nested loop) to curr_sum 
        and updating the maximum value.
TIME COMPLEXITY: O(n^2)
SPACE COMPLEXITY: O(1)
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len([True for n in nums if n < 0]) == len(nums):
            return max(nums)
        subarr, result = 0, pow(-10,5)
        for i in range(len(nums)):
            if nums[i] + subarr > 0:
                subarr += nums[i]
            else:
                subarr = 0
            result = max(result, subarr)
        
        return result

"""
TECHNIQUE: DP (Kadane's algorithm)
PROCEDURE:
1. Initialize the sum of current subarray (subarr) with the first element.
2. Create a for loop from the array[1]. Within the loop:
    2.1 If adding subarr to the array[i] is greater than array[i], update subarr to include the element.
    2.2 If adding subarr to the array[i] is less than array[i], update subarr to array[i]. This will start a new 
        subarray with array[i] and start tracking its sum.
    2.3 Update the maximum sum with the subarr calculated.
3. Return the maximum sum so far.
TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
NOTE: If the problem has only positive values, it becomes trivial. Including any integer is going to add to the sum.
    If we skip any value within the array, the sum would definitely be less than if it was included. 

    In this problem, negative values are also included. Including a negative value within the current subarray will reduce
    the current sum, but its possible that the sum may increase if we extend the subarray. 
    How do we determine if we should extend the subarray:
        If adding the sum of , extend the subarray to include the element.
        If adding the sum of subarray so far to the element decreases the sum, start a new subarray from this element.
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subarr, result = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] + subarr >= nums[i]:
                subarr += nums[i]
            else:
                subarr = nums[i]
            result = max(result, subarr)
        
        return result


        
