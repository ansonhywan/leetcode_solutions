class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            y = -(heapq.heappop(stones))
            x = -(heapq.heappop(stones))
            if x != y:
                z = -(y - x)
                heapq.heappush(stones, z)

        return -stones[0] if len(stones) == 1 else 0
