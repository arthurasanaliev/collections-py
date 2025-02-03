class CircularQueue:
    def __init__(self, k: int):
        self.size = k
        self.arr = [-1] * self.size
        self.start = 0
        self.end = 0

    def en_queue(self, value: int) -> bool:
        if self.is_full():
            return False
        self.arr[self.end] = value
        self.end = (self.end + 1) % self.size
        return True

    def de_queue(self) -> bool:
        if self.is_empty():
            return False
        self.arr[self.start] = -1
        self.start = (self.start + 1) % self.size 
        return True

    def front(self) -> int:
        return self.arr[self.start]

    def end(self) -> int:
        return self.arr[(self.end + self.size - 1) % self.size]

    def is_empty(self) -> bool:
        return self.start == self.end and self.arr[self.start] == -1

    def is_full(self) -> bool:
        return self.start == self.end and self.arr[self.start] != -1