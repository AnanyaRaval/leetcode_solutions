#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        m, n = len(haystack), len(needle)
        TECHNIQUE: Sliding window, brute force
        PROCEDURE:
        <corner: if len(needle) > len(haystack), return False>
        1. Run a loop over haystack characters.
        2. If haystack char == first char of needle:
            <early break: if len of remaining haystack chars < len(needle)> 
            2.1 Run a loop over needle chars.
            2.2. Run loop till haystack chars == needle chars
            2.2. if yes, return start index of needle substring in haystack. If no, continue the loop.
            2.3 Increment haystack pointer by 1. Need to compare next char and not skip over already compared chars.
        3. If all haystack chars have been seen, return -1. 

        TIME COMPLEXITY: O(m * n)
        SPACE COMPLEXITY: O(1)
        """

        m, n = len(haystack), len(needle)
        if n > m:
            return -1
        
        h_ptr = 0
        while h_ptr < m:
            n_ptr, h_idx = 0, h_ptr
            if m - h_idx < n:
                return -1
            while h_idx < m and n_ptr < n and haystack[h_idx] == needle[n_ptr]:
                h_idx += 1
                n_ptr += 1

            if n_ptr == n:
                return h_idx - n
            h_ptr += 1

        return -1

class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Cleaner version of the above code using for loops.
        TIME  COMPLEXITY: O(m*n)
        SPACE COMPLEXITY: O(1)
        """

        m, n = len(haystack), len(needle)
        for i in range(m-n+1):
            for j in range(n):
                if haystack[i+j] != needle[j]:
                    break
                if j == n-1:
                    return i
        return -1

class Solution3:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Can we use more pythonic code?
        TIME  COMPLEXITY: O(m*n)
        SPACE COMPLEXITY: O(m*n) Creates a new string everytime when slicing.
        """

        m,n = len(haystack), len(needle)
        for i in range(m - n +1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

class Solution4:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        TECHNIQUE: Unoptimized Rabin Karp (without modulo and rolling hash)
        PROCEDURE:
        m = len(haystack), n = len(needle)
        1. Create a function which takes substring as input and calculates a hash.
            1.1 For each char at index idx in the string, get its offset within a-z
            1.2 Multiply this offset by 26^n-1-idx,
            1.2 Calculate a sum of these representations and return as hash.
        2. Calculate hash(needle).
        3. Run a loop over haystack characters. 
            3.1 For every char, calculate hash of n sized substring starting with this char.
            3.1 If hash(n-sized substring) matches the hash(needle), match every char 
                between this substring and needle.
            3.2 If every char matches, return index of start char.
            3.3 if hash(n-sized substring) doesn't match hash(needle), continue for loop.
                No need to match.
        TIME COMPLEITY: O(m*n)
        SPACE COMPLEXITY: O(1)
        NOTE: We use 26 because: Mathematically, it turns out that to have a unique hash value 
            for every m-substring, positional weight should be greater than or equal to the number of 
            chars in the set, which is 26 for us. 
            https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/editorial/

        """
    
        def get_hash(substr:str) -> int:
            val, n = 0, len(needle) - 1
            for i in range(len(substr)):
                h = ord(substr[i]) - ord('a')
                val = (val + (h * (26^n)))
                n -= 1
            return val

        needle_hash = get_hash(needle)
        for h_ptr in range(len(haystack)-len(needle)+1):
            hay_hash = get_hash(haystack[h_ptr: h_ptr+len(needle)])
            if hay_hash == needle_hash:
                for i in range(len(needle)):
                    if needle[i] != haystack[i+h_ptr]:
                        break
                if i == len(needle)-1:
                    return h_ptr
        return -1