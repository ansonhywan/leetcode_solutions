class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        result = []
        c = 0
        for kv in sorted_freq:
            if c < k:
                result.append(kv[0])
            c += 1

        return result
    