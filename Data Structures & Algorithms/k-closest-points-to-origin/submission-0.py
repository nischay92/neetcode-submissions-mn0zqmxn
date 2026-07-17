import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts = []
        for x , y in points:
            dist = (x**2 + y**2)
            pts.append([dist, x, y])
        heapq.heapify(pts)
        res = []
        while k > 0:
            dist , x, y = heapq.heappop(pts)
            res.append([x , y])
            k -= 1
        return res
