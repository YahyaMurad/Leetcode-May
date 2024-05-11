import heapq

class Solution:
    def mincostToHireWorkers(self, quality, wage, k):
        workers = sorted((w / q, q, w) for q, w in zip(quality, wage))
        res = float("INF")
        sum_quality = 0
        queue = []

        for ratio, quality, wage in workers:
            heapq.heappush(queue, -quality)
            sum_quality += quality

            if len(queue) > k:
                sum_quality += heapq.heappop(queue)

            if len(queue) == k:
                res = min(res, ratio * sum_quality)

        return res
