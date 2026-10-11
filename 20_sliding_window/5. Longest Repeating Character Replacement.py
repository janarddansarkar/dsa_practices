"""
Author : janarddan
File_name = 5. Longest Repeating Character Replacement.py
Date : 16/07/26
Description :
LeetCode 424

Problem

You are given a string s consisting of uppercase English letters and an integer k.

You can replace at most k characters in the string with any other uppercase English letter.

Return the length of the longest substring you can obtain that contains only the same letter after performing at most k replacements.

** Example 1 **

Input:
s = "ABAB"
k = 2

Output:
4

Explanation:
Replace the two 'A's with 'B's (or vice versa).
Result: "BBBB"

** Example 2 **

Input:
s = "AABABBA"
k = 1

Output:
4

Explanation:
Replace one 'A' with 'B':

AABABBA
  ↓
AABBBBA

The longest repeating substring is "BBBB".

"""


def longestRepeating(s,k):
    if len(s) <= 1:
        return len(s)

    left = 0
    maxi = 0
    count = {}
    for right in range(len(s)):
        if s[right] not in count:
            count[s[right]] = 1
        else:
            count[s[right]] += 1

        curr_window_size = right - left + 1
        # Invalid window
        if curr_window_size - max(count.values()) > k:
            count[s[left]] -= 1
            left += 1

        curr_window_size_after_shrinking = right - left + 1
        maxi = max(maxi, curr_window_size_after_shrinking)

    return maxi

if __name__ == '__main__':
    print(longestRepeating('ABAB',2))
    print(longestRepeating('AABABBA',1))
    print(longestRepeating('AC',0))

"""
Approach / Logic:

We use the Sliding Window technique.

The idea is to maintain a window [left ... right] such that we can make
all characters inside the window the same using at most k replacements.

For example:

```
s = "AABABBA", k = 1
```

Consider the window:

```
"AABA"
```

Character frequencies:
A -> 3
B -> 1

The most frequent character is A (frequency = 3).

The remaining characters (B) need to be replaced with A.

Number of replacements required:

```
window_size - maximum_frequency
= 4 - 3
= 1
```

Since k = 1, this window is valid.

## KEY IDEA:

For any window:

```
replacements_required = window_size - max_frequency
```

Why?

Suppose the window is:

```
"AABAB"
```

Frequency:
A -> 3
B -> 2

If we want the entire window to become "AAAAA", we keep the 3 A's
and replace the 2 B's.

Therefore:

```
replacements_required = 5 - 3 = 2
```

## SLIDING WINDOW LOGIC:

1. Start with:

   ```
   left = 0
   right = 0
   ```

   and maintain a dictionary `count` to store the frequency of each
   character inside the current window.

2. Expand the window by moving `right`.

   ```
   count[s[right]] += 1
   ```

3. Calculate the current window size:

   ```
   right - left + 1
   ```

4. Find the frequency of the most common character:

   ```
   max(count.values())
   ```

5. Calculate how many replacements are required:

   ```
   curr_window_size - max(count.values())
   ```

6. If replacements required > k, the current window is invalid.

   Therefore, shrink the window from the left:

   ```
   count[s[left]] -= 1
   left += 1
   ```

7. After making the window valid, calculate its size and update `maxi`:

   ```
   maxi = max(maxi, right - left + 1)
   ```

8. Continue until `right` reaches the end of the string.

The largest valid window found is the answer.

## WHY `window_size - max_frequency`?

We only need to keep the most frequent character unchanged.

Every other character in the window must be replaced by that character.

For example:

```
Window = "AABAC"

A -> 3
B -> 1
C -> 1

Window size = 5
Maximum frequency = 3
```

So:

```
replacements required = 5 - 3 = 2
```

We can replace B and C with A:

```
AABAC
  ↓
AAAAA
```

## VALID / INVALID WINDOW:

If:

```
window_size - max_frequency <= k
```

the window is VALID because we can make all characters the same
using at most k replacements.

If:

```
window_size - max_frequency > k
```

the window is INVALID, so we shrink it from the left.

## IMPORTANT OBSERVATION:

We do not need to try every possible character or actually perform
the replacements.

We only need to know:

```
1. Size of the current window
2. Frequency of the most frequent character
```

That is enough to determine whether the window can be converted into
a repeating-character substring using at most k replacements.

## TIME COMPLEXITY:

In this implementation:

```
max(count.values())
```

takes O(26) because there are only 26 uppercase English letters.

Since 26 is a constant:

```
O(26) ≈ O(1)
```

The right pointer moves from left to right once, and the left pointer
also moves from left to right at most once.

Therefore:

```
Time Complexity = O(n)
```

where n is the length of the string.

## SPACE COMPLEXITY:

The `count` dictionary stores frequencies of uppercase English letters.

At most 26 characters can be stored:

```
Space Complexity = O(26) ≈ O(1)
```

## OVERALL:

Sliding Window
↓
Expand window using `right`
↓
Update character frequency
↓
Calculate:
window_size - max_frequency
↓
If replacements > k
↓
Shrink window using `left`
↓
Update maximum valid window length
↓
Return `maxi`

"""
