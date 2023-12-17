class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        hash_table = dict()

        if len(pattern) != len(words) or len(set(pattern)) != len(set(words)):
            return False
        
        for idx, word in enumerate(words):
            if word not in hash_table:
                hash_table[word] = pattern[idx]
            elif hash_table[word] != pattern[idx]:
                return False

        return True

"""
This Python function `wordPattern` checks if a string `s` follows a specific pattern given by the string `pattern`. The function returns `True` if `s` follows the pattern and `False` otherwise. Let's break down how it works and then discuss its time and space complexity with an example.

### Function Explanation:

1. **Splitting the String:** 
   - `words = s.split(' ')` splits the input string `s` into a list of words based on spaces.

2. **Initial Checks:**
   - `if len(pattern) != len(words) or len(set(pattern)) != len(set(words)):` checks two conditions:
     - If the length of `pattern` is not equal to the number of words in `s`, the pattern cannot match.
     - If the number of unique characters in `pattern` does not match the number of unique words in `s`, the pattern cannot match.

3. **Mapping and Checking:**
   - The function iterates over each word in `words`. 
   - For each word, it either adds a new entry to the `hash_table` with the word as the key and its corresponding pattern character as the value, or it checks if the existing entry for the word matches the current pattern character.
   - If there is a mismatch, it returns `False`.

4. **Return Value:**
   - If the function completes the loop without finding a mismatch, it returns `True`, indicating that the pattern matches.

### Example:

Consider `pattern = "abba"` and `s = "dog cat cat dog"`.

- Split `s` into words: `["dog", "cat", "cat", "dog"]`.
- Both `pattern` and `words` have equal lengths (4), and both have 2 unique elements (`'a', 'b'` and `"dog", "cat"`).
- Mapping:
  - Map `"dog"` to `'a'`.
  - Map `"cat"` to `'b'`.
  - Check `"cat"` is mapped to `'b'` (it is).
  - Check `"dog"` is mapped to `'a'` (it is).
- The pattern is followed, so return `True`.

### Time Complexity:

- The time complexity is **O(N)**, where N is the number of words in `s`.
- This is because the function iterates once over the list of words, performing constant time operations for each word.

### Space Complexity:

- The space complexity is **O(M + K)**.
- **O(M)** for the `words` list, where M is the number of characters in `s`.
- **O(K)** for the `hash_table`, where K is the number of unique words in `s`.
- Since the number of unique words can be at most equal to the number of words, this can also be considered as **O(N)** in the worst case.

In summary, the function is efficient with linear time complexity and potentially linear space complexity, depending on the input string's length and the number of unique words it contains.
"""