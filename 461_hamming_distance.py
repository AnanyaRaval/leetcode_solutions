#https://leetcode.com/problems/hamming-distance/description/
"""
TECHNIQUE: Bit counting
PROCEDURE:
1. Do an XOR operation between 2 integers. This will indicate bits which are different in both integers.
2. Count the number of 1's in xor. While xor is not zero:
    2.1 Check if the rightmost bit of xor is 1 by masking with 1.
    2.2 If the last bit is set, it will add 1 to the result.
    2.3 If the last bit is unset, it will add 0 to the result.
    2.4 Right shift xor by 1 bit. This will shift second last bit to last bit.
Loop will run till no bits within xor are set.
TIME COMPLEXITY: O(1)
SPACE COMPLEXITY: O(1)
"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        result = 0
        while xor:
            result += (xor & 1)
            xor = xor >> 1
        return result

"""
Use internal python function to count number of bits set to 1.
TIME COMPLEXITY: O(1)
SPACE COMPLEXITY: O(1)
"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:     
        return bin(x ^ y).count('1')
