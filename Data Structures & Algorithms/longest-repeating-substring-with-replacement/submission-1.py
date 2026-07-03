class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        result = 0
        charSet = {}
        maxf = 0
        for r in range(len(s)):
            charSet[s[r]] = 1 + charSet.get(s[r],0)
            maxf = max(maxf, charSet[s[r]])
            while (r - l + 1) - maxf > k:
                charSet[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
        return result

            