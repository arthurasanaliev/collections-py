class MyCircularQueue:
    def __init__(self, k: int):
        self.size = k
        self.arr = [-1] * self.size
        self.start = 0
        self.end = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.arr[self.end] = value
        self.end = (self.end + 1) % self.size
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.arr[self.start] = -1
        self.start = (self.start + 1) % self.size 
        return True

    def Front(self) -> int:
        return self.arr[self.start]

    def Rear(self) -> int:
        return self.arr[(self.end + self.size - 1) % self.size]

    def isEmpty(self) -> bool:
        return self.start == self.end and self.arr[self.start] == -1

    def isFull(self) -> bool:
        return self.start == self.end and self.arr[self.start] != -1