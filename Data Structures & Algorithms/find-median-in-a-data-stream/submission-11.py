class MedianFinder:

    def __init__(self):
        self.heap1 = []
        self.heap2 = []
        self.median = None
        self.mid = None
    def addNum(self, num: int) -> None:
        if self.median == None :
            self.median = self.mid = num
            return

        if num >= self.mid :
            heapq.heappush(self.heap1, num)
        
        elif num < self.mid :
            heapq.heappush(self.heap2, -num)        

        if len(self.heap1) - len(self.heap2) == 1:
            self.median = (self.mid+self.heap1[0])/2

        elif len(self.heap1) - len(self.heap2) == 2 :
            heapq.heappush(self.heap2, -self.mid)
            self.mid = self.median = heapq.heappop(self.heap1)

        elif len(self.heap2) - len(self.heap1) == 1:
            self.median = (self.mid-self.heap2[0])/2
            
        elif len(self.heap2) - len(self.heap1) == 2 :
            heapq.heappush(self.heap1, self.mid)
            self.mid = self.median = -heapq.heappop(self.heap2)  
        

        elif len(self.heap2) == len(self.heap1) :
            self.median = self.mid

    def findMedian(self) -> float:
        return self.median
