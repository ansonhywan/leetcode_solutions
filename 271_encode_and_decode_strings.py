class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = " "
        for s in strs:
            res += (str(len(s)) + '#' + s)
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0 # current position in string
        j = 0 

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
          
            l = int(s[i:j]) # length of string to be decoded
            i = j + 1
            j = i + l
            res.append(s[i:j])
            i = j
        return res        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
