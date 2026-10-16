"""
Author : janarddan
File_name = 13. Fruit Into Baskets.py
Date : 15/10/26
Description :

Leetcode 904. Fruit Into Baskets

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented
by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit.
There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree)
while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.


** Example 1: **

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

** Example 2: **

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].

** Example 3: **

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].


"""
from unittest.util import sorted_list_difference


class Solution:
    def totalFruit_better(self, fruits: list[int]) -> int:
        """
        TC -> O(n) + O(n) ~ O(n)
        SC -> O(1)
        """
        n = len(fruits)

        maxi = 0
        left = 0
        fruits_dict = {}

        for right in range(n): # Runs n times -> O(n)
            fruits_dict[fruits[right]] = fruits_dict.get(fruits[right], 0) + 1
            # Shrink until the window contains at most 2 types
            while len(fruits_dict) > 2: # O(n) total across all iterations
                fruits_dict[fruits[left]] -= 1
                if fruits_dict[fruits[left]] == 0:
                    del fruits_dict[fruits[left]]
                    # Remove the key when its count reaches 0;
                    # otherwise, len(fruits_dict) would still count that fruit type.
                left += 1

            maxi= max(maxi, right - left + 1)


        return maxi

    def totalFruit_optimal(self, fruits: list[int]) -> int:
        """
        TC -> O(n)
        SC -> O(1)
        """
        n = len(fruits)

        maxi = 0
        left = 0
        fruits_dict = {}

        for right in range(n):  # O(n)
            fruits_dict[fruits[right]] = fruits_dict.get(fruits[right], 0) + 1
            if len(fruits_dict) > 2:
                fruits_dict[fruits[left]] -= 1
                if fruits_dict[fruits[left]] == 0:
                    del fruits_dict[fruits[left]]  # Otherwise, the fruit which has value 0 will also get counted in len
                left += 1

            maxi= max(maxi, right - left + 1)


        return maxi

if __name__ == "__main__":
    sol = Solution()
    print(sol.totalFruit_better([1, 2, 1]))
    print(sol.totalFruit_better([0, 1, 2, 2]))
    print(sol.totalFruit_better([1, 2, 3, 2, 2]))
    print()
    print(sol.totalFruit_optimal([1,2,1]))
    print(sol.totalFruit_optimal([0,1,2,2]))
    print(sol.totalFruit_optimal([1,2,3,2,2]))




