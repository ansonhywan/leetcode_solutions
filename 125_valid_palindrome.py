class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return True

        # Remove non alphanumeric digits and make all lowercase
        new_s = ""
        for c in s:
            if c.isalpha() or c.isdigit():
                new_s += c
        new_s = new_s.lower()

        l = 0
        r = len(new_s) - 1

        while l < r:
            if new_s[l] != new_s[r]:
                return False
            l += 1
            r -= 1
        
        return True
