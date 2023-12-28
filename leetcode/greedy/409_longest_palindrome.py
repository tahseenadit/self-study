class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_counter = Counter(s)
        odd = 0
        result = 0
        for v in s_counter.values():
            # Handle even occurances of character
            if v % 2 == 0: result += v
            else: # Handle odd occurances of character
                odd = 1 # In this step, we know for sure that there is a character with odd number of occurances. So, we flag it.
                result += (v-1) # Here, we take the even occurances from odd occurances of character
        
        return result + odd # We add odd. If odd is 1, it means we have characters with odd number of occurances. We only add 1 because we can only add a single instance of any one character from all the odd characters.


"""
Hypothesis Behind the Logic

Count Characters: Count the frequency of each character in the string. In a palindrome, characters must appear in pairs (except possibly one character, which can appear in the middle of an odd-length palindrome).

Utilize Even Counts Fully: Every even count of a character can be fully used in the palindrome. For example, if a character appears 4 times, all 4 can be part of the palindrome.

Handle Odd Counts: For characters that appear an odd number of times, one of two things happens:
- If there's no character already contributing an odd count to the palindrome, the largest odd count can contribute all but one of its instances to the palindrome. The remaining instance can be the center of the palindrome.
- If there's already a character with an odd count contributing to the palindrome, other characters with odd counts can only contribute their count minus one (to make it even).

Maximize Length: The algorithm maximizes the length of the palindrome by using as many characters as possible, following the constraints of palindrome formation.

Greedy Algorithm
A greedy algorithm makes the optimal choice at each step, aiming to find the overall optimal solution. In this case, the algorithm greedily uses all even counts and the largest odd count (if any), as these choices will always contribute to creating the longest possible palindrome.

Example Case 1:
Let's use the string s = "aabbcad" as an example:

Count Characters: {'a': 3, 'b': 2, 'c': 1, 'd': 1}
Even Counts: We have 'b': 2, so add 2 to result.
Odd Counts: We have three odd counts - 'a': 3, 'c': 1, and 'd': 1. We choose 'a' for its highest odd count, add 2 (3-1) to result, and set odd = 1.
Other Odd Counts: 'c' and 'd' can contribute 0 characters each (since their counts are 1, and we subtract 1).
Result: The length of the longest palindrome is result + odd = 2 (from 'b') + 2 (from 'a') + 1 (for the center 'a') = 5.
The longest palindrome that can be constructed from "aabbcad" is, for instance, "abcba" or "bacab", both of length 5.

Example Case 2:
Let's apply the same logic to the string s = "aabbcccad":

Step-by-Step Analysis
Count Characters: First, we count the frequency of each character.
s = "aabbcccad" results in the counts: {'a': 3, 'b': 2, 'c': 3, 'd': 1}
Even Counts: We use all characters that have an even count.
'b': 2 and 'c': 3 (we will adjust 'c' in the next step).
Add 2 (from 'b') to result. The total is now 2.
Odd Counts: We have two characters with odd counts - 'a': 3 and 'c': 3. We also have 'd': 1. We will take all but one of each odd count.
For 'a' and 'c', add 2 (3-1) each to result. The total is now 2 (from 'b') + 2 (from 'a') + 2 (from 'c') = 6.
odd = 1, as we can use one of the odd characters ('a', 'c', or 'd') as the center of the palindrome.
Result: The length of the longest palindrome is result + odd = 6 + 1 = 7

### Time Complexity: O(n)

1. Counting Characters: The algorithm iterates through each character of the string once to count the frequency of each character. This operation takes O(n) time, where n is the length of the string.

2. Iterating Over the Counter: After counting, the algorithm iterates over the character frequencies stored in the counter. The number of distinct characters in the string can be at most the length of the string itself. However, in most practical scenarios, especially when dealing with standard English text, the number of distinct characters (including both uppercase and lowercase letters) is significantly less than the length of the string. But for the sake of worst-case analysis, we consider this step also as O(n).

Therefore, the overall time complexity of the algorithm is O(n) + O(n), which simplifies to O(n).

### Space Complexity: O(1) or O(n)

The space complexity depends on how you consider the constraints of the problem:

1. Counter Space for English Alphabets: If the input string is composed only of English alphabet characters (both uppercase and lowercase), then the counter will at most have 26 + 26 = 52 entries, regardless of the length of the string. This is a constant number and does not scale with the size of the input. Hence, under this constraint, the space complexity is O(1), a constant space complexity.

2. Counter Space for Generic Input: If the input string can contain any possible character (i.e., not limited to the English alphabet), the number of unique characters could potentially scale with the length of the string. In the worst case, every character in the string is unique, and the counter would have as many entries as the length of the string. In this scenario, the space complexity is O(n).

### Conclusion

- Time Complexity: O(n), because the algorithm needs to iterate through the entire string once to count characters, and potentially again to process each character count.
- Space Complexity: 
  - O(1) if the input is limited to the English alphabet (or any fixed character set).
  - O(n) for a generic input where every character could be unique.
"""