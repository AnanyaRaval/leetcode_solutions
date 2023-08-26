# https://leetcode.com/problems/remove-element/

from typing import List

"""
TECHNIQUE: Two pointers
PROCEDURE:
1. Initialize ptr which points to the element being written. Only valid values will be assigned to this index.
2. Create a loop to go through all elements of nums (0 -> last index):
    2.1 If current element is not equal to the value to be removed (val), 
        assign this value index ptr. 
        Increment ptr to point to the next index to be written with a valid value.
3. Return ptr. Values in indices [0, ptr-1] are valid. At the end of the loop, ptr will point to the next 
    valid element to be written. Its also the number of values between [0, ptr-1] (since array are 0-indexed).
TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
Note: Loop invariant: [0, ptr-1] contains valid values. 
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ptr = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[ptr] = nums[i]
                ptr += 1
        return ptr

"""
TECHNIQUE: Two pointers
PROCEDURE:
1. Create 2 pointers start and end pointing to first and last indices of nums.
    end index will point to index where value to be removed (val) is stored.
    start index searches for val to be removed..
2. Create a for loop which runs till start and end indices cross each other:
    2.1 If value pointed by start index == val to be removed, swap this val with end index.
        (Now nums[end] == val). Increment end index to point to new index where val will be stored.
    2.2 If value pointed by start index != val to be removed, the array is valid till [0, start].
        Increment start index to check the next element in nums.
3. Return start. [0, start-1] is the valid array. So, the number of elements in the valid array 
                is start.
TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
NOTE: We are moving all occurances of val to be removed at the end of the array. 
Loop Invariant: [0, start-1] contains only valid values.
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start, end = 0, len(nums)-1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
            else:
                start += 1
        return start

"""
TECHNIQUE: Two pointers
TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1) 
NOTE: Remove swaps to reduce the number of assignments. The problem mentions that it doesn't care about elements
        after the valid values, we don't need to re-assign.
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start, end = 0, len(nums)-1
        while start <= end:
            if nums[start] == val:
                nums[start] = nums[end]
                end -= 1
            else:
                start += 1
        return start
