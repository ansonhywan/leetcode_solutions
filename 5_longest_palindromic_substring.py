class Solution:
    def longestPalindrome(self, s: str) -> str:
        def findPalindrome(res, res_len, odd):
            for i in range(len(s)):
                if odd:
                    l, r = i, i
                else:
                    l, r = i, i + 1
                while (
                    l >= 0 and r < len(s) and s[l] == s[r]
                ):  # l and r are in bounds and are the same character
                    cur_len = r - l + 1
                    if cur_len > res_len:
                        res_len = cur_len
                        res = s[l : r + 1]
                    l -= 1
                    r += 1

            return [res, res_len]

        res_odd = findPalindrome("", 0, True)
        res = findPalindrome(res_odd[0], res_odd[1], False)
        return res[0]
