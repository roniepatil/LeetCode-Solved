'''
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
'''
from typing import List
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        window = {}
        T = {}
        have = 0
        for i in set(t):
            T[i] = t.count(i)
        for i in set(t):
            window[i] = 0
        need = len(T)
        l = 0
        res = (0,0)
        len_res = len(s) + 1
        for r in range(len(s)):
            if s[r] in window:
                window[s[r]] = 1 + window.get(s[r], 0)
                if window[s[r]] == T[s[r]]:
                    have += 1
            while need == have:
                curr_res = (l,r)
                curr_len = r - l + 1
                # print(curr_res)
                if curr_len < len_res:
                    len_res = curr_len
                    res = curr_res
                if s[l] in window:
                    window[s[l]] -= 1
                    if window[s[l]] < T[s[l]]:
                        have -= 1
                l += 1
        return s[res[0]:res[1]+1] if len_res != float("infinity") else ""
        # if t == "" : return ""
        # window, countT = {}, {}
        # for i in t:
        #     countT[i] = 1 + countT.get(i,0)
        # l = 0
        # have, need = 0, len(countT)
        # res, min_len = [-1,-1], float("infinity")

        # for r in range(len(s)):
        #     c = s[r]
        #     window[c] = 1 + window.get(c, 0)

        #     if c in countT and countT[c] == window[c]:
        #         have += 1

        #     while have == need:
        #         if (r-l+1) < min_len:
        #             min_len = r-l+1
        #             res = [l,r]
        #         window[s[l]] -= 1
        #         if s[l] in countT and window[s[l]] < countT[s[l]]:
        #             have -= 1
        #         l += 1
        
        # l, r = res
        # return s[l:r+1] if min_len != float("infinity") else ""
            

s = "aa"
t = "aa"
a = Solution()
print(a.minWindow(s,t))