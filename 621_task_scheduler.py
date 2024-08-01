class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Use a heap / priority queue to prioritize tasks that need to be done

        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        q = (
            deque()
        )  # Holds a tuple with: (task count, time task is available to be run again)

        time = 0
        while maxHeap or q:
            time += 1

            if maxHeap:
                cur_count = heapq.heappop(maxHeap) + 1
                if cur_count < 0:
                    q.append((cur_count, time + n))

            if len(q) > 0 and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
