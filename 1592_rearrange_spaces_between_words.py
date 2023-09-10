# https://leetcode.com/problems/rearrange-spaces-between-words/description/

"""
TECHNIQUE: Loops
PROCEDURE:
1. Initialize variable `spaces` = 0 denoting the count of spaces in `text`.
2. Initialize variable `string` converting `text` to a list.
3. Initialize variable `words` to store the list of words found in `tex`t.
4. Initialize a variable `idx` = 0 to loop through the `string`.
4. Create a while loop to run till the end of `string`:
    4.1 Create a nested while loop which runs till value at `string[idx]` == ' ':
        Increment `spaces` to count the spaces.
        Increment loop counter `idx` to move to next element.
    4.2 Initialize the variable `word` to store the current word from `string`.
    4.3 Create a nested while loop which runs till value at `string[idx]` is not ' ', but in [a-zA-Z]:
        Append character `string[idx]` to `word`.
        Increment loop counter `idx` to move to next element.
    4.4 We have extracted a single word from `text` and stored it in `word`. 
        Append `word` to the list `words`.
5. Initialize a variable `gap` to store spaces between each word in `text`.
    If number of words in `words` is > 1, `gap` = `spaces` / `len(words)-1`.
        Divide by len(words)-1 since the spaces will be "between" words => len(words)-1.
    If number of words in `words` == 1, `gap` = 0. There is only 1 word.
6. Initialize a variable `last` to store extra spaces at the end.
    If number of words in `words` > 1, `last` = `spaces` % `(len(words)-1)`.
    If number of words in `words` == 1, `last` = `spaces`. Only 1 word => all spaces will be added at the end.
7. Initialize a variable `result` to store the result.
8. Create a for loop to go through the list `words`:
    8.1 Add current word `w` to result.
    8.2 Add `gap` number spaces after word `w`.
    8.3 If it is the last word, add `end` spaces after the last word.
9. Return `result`.
TIME COMPLEXITY: O(n)
SPACES COMPLEXITY: O(n)
"""
class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces, string, words = 0, list(text), []
        idx = 0
        while idx < len(string):
            while idx < len(string) and string[idx] == " ":
                spaces += 1
                idx += 1
            word = ""
            while idx < len(string) and string[idx] != " ":
                word += string[idx]
                idx += 1
            if word:
                words.append(word)

        gap = int(spaces / (len(words)-1)) if len(words) > 1 else 0
        last = spaces % (len(words)-1) if len(words) > 1 else spaces
        result = ""
        for i, w in enumerate(words):
            result += w
            if i == len(words)-1:
                result += (" "* last)
            else:
                result += (" "*gap)
        
        return result

"""
Replace nested while loops count() and split() functions.
Replace calculation of `gap` and `last` with divmod() function.
Replace for loop with join() function.
"""
class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = text.count(' ')
        words = text.split()
        if len(words) == 1:
            return ''.join(words+[' '*spaces])
        gap, last = divmod(spaces, len(words)-1)
        return (' '*gap).join(words) + ' '*last




        
