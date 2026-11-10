from heapq import heapify, heapify_max, heappop, heappop_max, heappush, heappush_max
class MedianFinder:

    def __init__(self):

        self.size_of_small = 0
        self.smallheap = []
        heapify_max(self.smallheap)

        self.size_of_big = 0
        self.bigheap = []
        heapify(self.bigheap)

    def addNum(self, num: int) -> None:
        #print("before: \n", "smallheap: ", self.size_of_small, self.smallheap, "\n", "bigheap: ", self.size_of_big, self.bigheap)
        if self.size_of_small == self.size_of_big == 0:
            heappush_max(self.smallheap, num)
            self.size_of_small += 1
            #print("after: \n", "smallheap: ", self.size_of_small, self.smallheap, "\n", "bigheap: ", self.size_of_big, self.bigheap, "\n")
            return
            
        if self.size_of_small == self.size_of_big != 0:
            if num < self.bigheap[0]:
                heappush_max(self.smallheap, num)
                self.size_of_small += 1
            if num >= self.bigheap[0]:
                heappush(self.bigheap, num)
                self.size_of_big += 1
            #print("after: \n", "smallheap: ", self.size_of_small, self.smallheap, "\n", "bigheap: ", self.size_of_big, self.bigheap, "\n")
            return
                

        if self.size_of_small - self.size_of_big == 1:
            if self.smallheap[0] > num:
                heappush_max(self.smallheap, num)
                heappush(self.bigheap, heappop_max(self.smallheap))
                self.size_of_big += 1
            else:
                heappush(self.bigheap, num)
                self.size_of_big += 1
            #print("after: \n", "smallheap: ", self.size_of_small, self.smallheap, "\n", "bigheap: ", self.size_of_big, self.bigheap, "\n")
            return

        if self.size_of_big - self.size_of_small == 1:
            if self.bigheap[0] > num:
                heappush_max(self.smallheap, num)
                self.size_of_small += 1
            else: 
                heappush(self.bigheap, num)
                heappush_max(self.smallheap, heappop(self.bigheap))
                self.size_of_small += 1
            #print("after: \n", "smallheap: ", self.size_of_small, self.smallheap, "\n", "bigheap: ", self.size_of_big, self.bigheap, "\n")
            return
        

    def findMedian(self) -> float:
        if self.size_of_small == self.size_of_big:
            return (self.smallheap[0] + self.bigheap[0]) / 2
        if self.size_of_small > self.size_of_big:
            return self.smallheap[0]
        return self.bigheap[0]
        
        

    