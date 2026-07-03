class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        result = 0
        charSet = {}

        for r in range(len(s)):
            charSet[s[r]] = 1 + charSet.get(s[r],0)
            
            while (r - l + 1) - max(charSet.values()) > k:
                charSet[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
        return result

            