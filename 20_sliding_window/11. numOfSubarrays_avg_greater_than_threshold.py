"""
Author : janarddan
File_name = 11. numOfSubarrays_avg_greater_than_threshold.py
Date : 11/10/26
Description :

Leetcode 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and
average greater than or equal to threshold.

** Example 1: **

Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively.
All other sub-arrays of size 3 have averages less than 4 (the threshold).

** Example 2: **

Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.

"""


class Solution:
    def numOfSubarrays_bruteforce(self, arr: list[int], k: int, threshold: int) -> int:
        """
        TC -> O(n*k)
        Worst case O(n*2) when k = Θ(n) (e.g. k = n/2)
        SC -> O(1)
        """

        n = len(arr)
        count = 0

        for left in range(n - k + 1):
            curr_sum = 0
            for right in range(left, left + k):
                curr_sum += arr[right]

            curr_avg = curr_sum / k
            if curr_avg >= threshold:
                count += 1

            #   ---  OR --- the below part ---
            # if curr_sum >= (k * threshold):
            #     count += 1

        return count

    def numOfSubarrays_optimal(self, arr: list[int], k: int, threshold: int) -> int:
        """
        TC -> O(n)
        SC -> O(1)
        """
        n = len(arr)
        count = 0

        left = 0

        total = 0

        for right in range(n):
            if (right - left + 1) > k:
                total -= arr[left]
                left += 1

            total += arr[right]

            if (right - left + 1) == k:
                curr_avg = total / k
                if curr_avg >= threshold:
                    count += 1

        return count

    def numOfSubarrays_optimal2(self, arr: list[int], k: int, threshold: int) -> int:
        """
        TC -> O(k) + O(n-k) ~ O(n)
        SC -> O(k) because arr[:k-1] creates a temporary slice
        """
        res = 0
        curSum = sum(arr[:k - 1]) # O(k)
        # arr[:k-1] creates a slice of k-1 elements
        # sum() then processes those k-1 elements

        for L in range(len(arr) - k + 1):  ## O(n - k) iterations
            curSum += arr[L + k - 1]

            if (curSum / k) >= threshold:
                res += 1

            curSum -= arr[L]

        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.numOfSubarrays_bruteforce(arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4))
    print(sol.numOfSubarrays_bruteforce([11,13,17,23,29,31,7,5,2,3], 3, 5
))
    print()
    print(sol.numOfSubarrays_optimal(arr=[2, 2, 2, 2, 5, 5, 5, 8], k=3, threshold=4))
    print(sol.numOfSubarrays_optimal(arr=[11, 13, 17, 23, 29, 31, 7, 5, 2, 3], k=3, threshold=5
                                        ))
    print()
    print(sol.numOfSubarrays_optimal2(arr=[2, 2, 2, 2, 5, 5, 5, 8], k=3, threshold=4))
    print(sol.numOfSubarrays_optimal2(arr=[11, 13, 17, 23, 29, 31, 7, 5, 2, 3], k=3, threshold=5
                                     ))




