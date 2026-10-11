"""
Author : janarddan
File_name = 9. Longest Substring Without Repeating Characters.py
Date : 21/09/26
Description :
Leetcode 3. Longest Substring Without Repeating Characters - (Medium)

Given a string s, find the length of the longest substring without duplicate characters.

** Example 1: **

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

** Example 2: **

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

** Example 3: **

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring_bruteforce1(self, s:str) -> int:
        """
        TC -> O(n**2)
        SC -> O(n)
        """
        n = len(s)
        maxi = 0

        for i in range(n): # O(n)
            seen = {} # SC -> O(n) for each i, can use the same space
            for j in range(i, n): # O(n)
                if s[j] in seen:
                    curr_len = (j-i+1)-1
                    maxi = max(curr_len, maxi)
                    break

                seen[s[j]] = j

                curr_len = j - i + 1
                maxi = max(maxi, curr_len)

        return maxi

    def lengthOfLongestSubstring_bruteforce2(self, s:str)->int:
        """
        TC -> O(n**2)
        SC -> O(n)
        """
        n = len(s)
        maxi = 0

        for i in range(n):
            seen = set() # SC -> O(n) for each i, can use the same space
            for j in range(i,n):
                if s[j] in seen:
                    break

                seen.add(s[j])
                maxi = max(maxi, j - i + 1)

        return maxi

    def lengthOfLongestSubstring_optimal(self, s: str) -> int:
        """
        TC -> O(n)
        SC -> O(n)
        """
        n = len(s)
        maxi = 0
        seen_d = {}
        left = 0

        for right in range(n):
            if s[right] in seen_d:
                left = max(left, seen_d[s[right]] + 1)

            seen_d[s[right]] = right
            maxi = max(maxi, right - left + 1)

        return maxi


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring_bruteforce1('abcabcbb'))
    print(sol.lengthOfLongestSubstring_bruteforce1('bbbb'))
    print(sol.lengthOfLongestSubstring_bruteforce1('pwwkew'))
    print(sol.lengthOfLongestSubstring_bruteforce1('abcde'))
    print()
    print(sol.lengthOfLongestSubstring_bruteforce2('abcabcbb'))
    print(sol.lengthOfLongestSubstring_bruteforce2('bbbb'))
    print(sol.lengthOfLongestSubstring_bruteforce2('pwwkew'))
    print(sol.lengthOfLongestSubstring_bruteforce2('abcde'))
    print()
    print(sol.lengthOfLongestSubstring_optimal('abcabcbb'))
    print(sol.lengthOfLongestSubstring_optimal('bbbb'))
    print(sol.lengthOfLongestSubstring_optimal('pwwkew'))
    print(sol.lengthOfLongestSubstring_optimal('abcde'))
