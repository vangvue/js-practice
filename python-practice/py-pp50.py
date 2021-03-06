# https://leetcode.com/problems/arranging-coins/
# 441. Arranging Coins

# You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

# Given n, find the total number of full staircase rows that can be formed.

# n is a non-negative integer and fits within the range of a 32-bit signed integer.

class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return n
        
        count = 0
        counter = 1
        
        while n > 0:
            n -= counter
            if n >= 0:
                count += 1
            counter += 1
                
        return count