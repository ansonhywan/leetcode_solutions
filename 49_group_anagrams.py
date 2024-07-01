class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resultDict = defaultdict(list)

        for s in strs:
            sorted_char = ''.join(sorted(s))
            resultDict[sorted_char].append(s)

        return resultDict.values()
