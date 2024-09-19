class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = cost[len(cost) - 1], 0

        for i in range(len(cost) - 2, -1, -1):
            temp = one
            cost[i] = min(cost[i] + one, cost[i] + two)
            one = cost[i]
            two = temp

        return min(cost[0], cost[1])
