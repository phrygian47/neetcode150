# Valid Palindrome

Given a string `s`, return `true` if it is a **palindrome**, otherwise return `false`.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters `(A-Z, a-z)` and numbers `(0-9)`.

# Example 1

```python
Input: s = "Was it a car or a cat I saw?"

Output: True
```

# Example 2

```python
Input: s = "tab a cat"

Output: False
```

## Constraints

- `1 <= s.length <= 1000`
- `s` is made up of only printable ASCII characters.

# My Solution

This problem is pretty straightforward, the main thing we must do is make sure to skip any non alphanumeric characters, such as whitespace or symbols. Python has a built in method for this `.isalnum()`, but you can also build your own helper function using `ord()`. We can use two pointers for this solution, one starting at the start of the input string, and the other and the end. then we check if both pointers are pointing to an alphanumeric character, if no we increment the left pointer, or decrement the right pointer, until they are both alphanumeric. Once both are alphanumeric, we simply check if they are the same character, if not we return false, otherwise we increment the left pointer and decrement the right pointer to go to the next character in the string. If we exit the loop, then we know we have a valid palindrome.

## Code

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
```

## Time and & Space Complexity

This algorithm runs in O(n) time and takes O(1) extra space.
