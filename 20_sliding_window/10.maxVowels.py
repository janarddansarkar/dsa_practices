"""
Author : janarddan
File_name = 10.maxVowels.py
Date : 11/10/26
Description :

Leetcode 1456. Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

** Example 1: **

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

** Example 2: **

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

** Example 3: **

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

"""

class Solution:
    def maxVowels_bruteforce(self, s: str, k: int) -> int:
        """
        TC -> O(n*k)
        Worst case -> O(n²), when k = O(n)
        SC -> O(1), for only the vowels and other variables
        """
        n = len(s)
        maxi = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for i in range(n - k + 1):
            curr_count = 0
            for j in range(i, i + k):
                if s[j] in vowels:
                    curr_count += 1

            maxi = max(maxi, curr_count)

        return maxi

    def maxVowels_optimal(self, s: str, k:int)->int:
        """
        TC -> O(n)
        SC -> O(1)
        """
        n = len(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}

        maxi = 0
        curr_count = 0
        left = 0

        for right in range(n): # O(n)
            if s[right] in vowels: # O(1), set lookup takes O(1)
                curr_count += 1

            if right - left + 1 > k:
                if s[left] in vowels: # O(1), set lookup takes O(1)
                    curr_count -= 1
                left += 1

            maxi = max(maxi, curr_count)

        return maxi


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxVowels_bruteforce('abciiidef', 3))
    print(sol.maxVowels_bruteforce('aeiou', 2))
    print(sol.maxVowels_bruteforce('leetcode', 3))
    print()
    print(sol.maxVowels_optimal('abciiidef', 3))
    print(sol.maxVowels_optimal('aeiou', 2))
    print(sol.maxVowels_optimal('leetcode', 3))


