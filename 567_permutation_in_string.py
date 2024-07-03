class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_freq = 26 * [0]
        s2_freq = 26 * [0]
        for i in range(len(s1)):
            s1_freq[ord(s1[i]) - ord("a")] += 1
            s2_freq[ord(s2[i]) - ord("a")] += 1
        
        matches = 0

        for i in range(26):
            if s1_freq[i] == s2_freq[i]:
                matches += 1

        l = 0
        r = l + len(s1) - 1

        while l < len(s2)-len(s1):
            if matches == 26:
                return True
            
            i = ord(s2[l]) - ord("a")
            # Update s2_freq and matches with removal of character at start of window
            s2_freq[i] -= 1
            if s1_freq[i] == s2_freq[i]:
                matches += 1
            elif s1_freq[i] - 1 == s2_freq[i]:
                matches -= 1

            # Update pointers to create new window
            l += 1
            r += 1

            # Update s2_freq and matches with new character at end of window
            i = ord(s2[r]) - ord("a")
            s2_freq[i] += 1
            if s1_freq[i] == s2_freq[i]:
                matches += 1
            elif s1_freq[i] + 1 == s2_freq[i]:
                matches -= 1
        
        return matches == 26
