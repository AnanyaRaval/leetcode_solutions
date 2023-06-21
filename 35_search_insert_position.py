#https://leetcode.com/problems/search-insert-position/description/
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        TECHNIQUE: Linear scan
        PROCEDURE: 
        1. Run a loop over nums
            1.1 If value == target, return its index.
            1.2 If value < target, continue the loop.
            1.3 If value > target, this is the first value which 
                is greater than target. return its index.
        <corner: If loop is over, target is greater than all values 
        in nums. return len(nums) as the next index where 
        target would be inserted>
        TIME COMPLEXITY: O(n)
        SPACE COMPLEXITY: O(n)
        """
        
        for idx in range(len(nums)):
            if nums[idx] >= target:
                return idx
        return len(nums) #corner

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Can we make use of the fact that array is sorted? 
        TECHNIQUE: Binary search
        PROCEDURE:
        1. Take 2 pointers at the start and end of nums.
            1.1 Calculate mid point of the nums.
            1.2 If value at mid == target, return mid.
            1.3 If value at mid < target, move start to mid+1
            1.4 If value at mid > target, move end to mid-1
        2. The loop breaks at end > start. start is moving towards first value < target and end is moving towards first value > target. When start == end, they both meet at the first value > target, which is why we need to move end again. Hence, we return start index.
        TIME COMPLEXITY: O(n)
        SPACE COMPLEXITY: O(n)
        """

        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid+1
            else:
                end = mid-1
        return start