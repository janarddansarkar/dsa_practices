"""
Author : janarddan
File_name = 12. Max Consecutive Ones III.py
Date : 13/10/26
Description :

Leetcode 1004. Max Consecutive Ones III

Given a binary array nums and an integer k, return the maximum number of consecutive
1's in the array if you can flip at most k 0's.

** Example 1: **

Input: nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2
Output: 6
Explanation: [ 1, 1, 1, 0, 0, '1', 1, 1, 1, 1, '1']
numbers within '' were flipped from 0 to 1.

** Example 2: **

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

"""

class Solution:
    def longestOnes_bruteforce(self, nums: list[int], k: int) -> int:
        n = len(nums)
        maxi = 0

        for left in range(n):
            curr_len = 0
            zeros_flipped = 0

            for right in range(left, n):

                if nums[right] == 0:
                    zeros_flipped += 1

                if zeros_flipped > k:
                    break

                curr_len += 1

            maxi = max(curr_len, maxi)

        return maxi

    def longestOnes_optimal(self, nums: list[int], k: int) -> int:
        n = len(nums)

        left = 0
        curr_max = 0
        maxi = 0
        zeros_flipped = 0

        for right in range(n):

            if nums[right] == 0:
                zeros_flipped += 1

            while zeros_flipped > k:
                if nums[left] == 0:
                    zeros_flipped -= 1
                left += 1

            curr_max = right - left + 1
            maxi = max(curr_max, maxi)

        return maxi


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestOnes_bruteforce([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
    print(sol.longestOnes_bruteforce([1, 1, 1, 0, 0, 1, 1], 2))
    print(sol.longestOnes_bruteforce([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
    print()
    print(sol.longestOnes_optimal([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
    print(sol.longestOnes_optimal([1, 1, 1, 0, 0, 1, 1], 2))
    print(sol.longestOnes_optimal([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))

