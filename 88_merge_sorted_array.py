#https://leetcode.com/problems/merge-sorted-array/

from typing import List

"""
TECHNIQUE: Brute Force
ALGORITHM:
1. Copy nums2 to the the last n indices of nums1.
2. Sort nums1 in-place using internal Python function.
TIME COMPLEXITY: O((m+n) log(m+n))
SPACE COMPLEXITY: O(1)
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2
        nums1.sort()

"""
TECHNIQUE: 2 pointers.
ALGORITHM:
1. Copy nums1 to a temporary list temp.
2. Initialize 2 pointers i and j to traverse nums1 and nums2 respectively.
3. Create a for loop to populate the combined m+n elements. Within the for loop:
    3.1 If all elements of nums1 are populated, populate with current nums2 element(nums2[j]).
        Increment j by 1 to move to next nums1 element.
    3.2 If all elements of nums1 are populated, populate with current nums1 element(temp[i]).
        Increment i by 1 to move to the next nums2 element.
    3.3 Compare current nums1 element (temp[i]) with current nums2 element (nums2[j]). 
        If temp[i] is less in value, populate nums1 with temp[i]. Increment i to compare next element of temp.
        If nums2[j] is less in value, populate nunms1 with nums2[j]. Increment j to compare next element of nums2
TIME COMPLEXITY: O(m+n)
SPACE COMPLEXITY: O(m)
NOTE: We need a temporary array to store original sorted nums1 as we will be overwriting nums1
        with sorted elements after merging nums1 and nums2.
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        temp,i,j = nums1[:], 0, 0
        for ptr in range(m+n):
            if i >= m and j < n:
                nums1[ptr] = nums2[j]
                j += 1
            elif j >= n and i < m:
                nums1[ptr] = temp[i]
                i += 1
            elif temp[i] <= nums2[j]:
                nums1[ptr] = temp[i]
                i += 1
            else:
                nums1[ptr] = nums2[j]
                j += 1

"""
Can we do it with O(1) space complexity?
NOTE: The trick here is to fill nums1 from the the end and start comparing nums1 with nums2 from the end of array.
        This way we can compare both arrays while overwriting elements of nums1. 
        We get the correct result because the current element of nums1 being compared will not be the one being overwritten.
        The only time the element being compared with the element being overwritten in nums1 is the same is when 
        all elements of nums2 have been considered. In this scenario, only elements of nums1 are left and they are being overwritten
        with themselves.
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, ptr = m-1, n-1, len(nums1)-1

        while ptr >= 0:
            if i < 0:
                nums1[ptr] = nums2[j]
                j -= 1
            elif j < 0:
                nums1[ptr] = nums1[i]
                i -= 1
            elif nums1[i] <= nums2[j]:
                nums1[ptr] = nums2[j]
                j -= 1
            else:
                nums1[ptr] = nums1[i]
                i -= 1
            ptr -= 1

"""
Can we reduce the if conditions?
Combine if conditions where we initialize using nums2. 
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = m-1, n-1
        for ptr in range(m+n-1,-1,-1):
            if j < 0:
                break
            if i < 0 or (nums1[i] <= nums2[j]):
                nums1[ptr] = nums2[j]
                j -= 1
            else:
                nums1[ptr] = nums1[i]
                i -= 1

