class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        heapq.heapify(minHeap)

        for point in points:
            e_dist = self.e_dist_from_origin(point)
            heapq.heappush(minHeap, (e_dist, point))

        res = []
        for _ in range(k):
            res.append(heapq.heappop(minHeap)[1])

        return res

    def e_dist_from_origin(self, point) -> int:
        return math.sqrt(pow(point[1], 2) + pow(point[0], 2))
