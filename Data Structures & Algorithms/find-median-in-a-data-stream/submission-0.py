class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        # check if num fits correctly in either small or large
        if self.small and self.large and (-1 * self.small[0] >= self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # if the heaps are uneven size
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small):
            val = -1 * heapq.heappop(self.large)
            heapq.heappush(self.small, val)
        

    def findMedian(self) -> float:
        # if the lens are odd or even
        if len(self.small) > len(self.large):
            return (-1 * self.small[0])
        if len(self.small) < len(self.large):
            return self.large[0]
        return ((-1 * self.small[0] + self.large[0]) / 2)
        
        