# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters

from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        ans = 0
        for mask in range(1 << n):
            seen = set()
            isValid = True
            strSize = 0
            for i in range(n):
                if (mask >> i) & 1 == 0: continue
                for c in arr[i]:
                    if c in seen:   # If c is already existed then it's invalid subsequence.
                        isValid = False
                        break
                    seen.add(c)  # mark as character `c` is already seen
                    strSize += 1
                if not isValid: break  # prune when there is a duplicate
            if isValid and strSize > ans:
                ans = strSize
        return ans
