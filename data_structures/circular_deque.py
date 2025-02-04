class MyCircularDeque:
    def __init__(self, k: int):
        self.size = k
        self.count = 0
        self.arr = [-1] * self.size 
        self.start = 0
        self.end = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.arr[self.end] = value 
            self.count += 1
            return True
        
        self.start = (self.start + self.size - 1) % self.size 
        self.arr[self.start] = value
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.arr[self.start] = value
            self.count += 1
            return True

        self.end = (self.end + self.size + 1) % self.size
        self.arr[self.end] = value
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.arr[self.start] = -1
        self.start = (self.start + self.size + 1) % self.size
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.arr[self.end] = -1
        self.end = (self.end + self.size - 1) % self.size
        self.count -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.arr[self.start]

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.arr[self.end]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size 