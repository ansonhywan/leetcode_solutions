class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charFreq = {}
        l = 0
        maxLength = 0

        for r in range(len(s)):
            charFreq[s[r]] = 1 + charFreq.get(s[r], 0)

            while (r - l + 1) - max(charFreq.values()) > k:
                # While invalid sliding window
                charFreq[s[l]] -= 1
                l += 1

            maxLength = max(maxLength, r - l + 1)


        return maxLength
    