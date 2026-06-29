class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxLength = 0
        charSet = set()

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            maxLength = max(r - l + 1, maxLength)
        return maxLength
        # while r < len(s):
        #     if s[r] in charSet:
        #         l = r
        #         r += 1
        #         temp = 0
        #     else:
        #         temp += 1
        #         maxLength = max(temp, maxLength)
        #         l += 1
        #         r += 1
        # return maxLength
