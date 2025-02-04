class CircularDeque:
    def __init__(self, k: int):
        self.size = k
        self.count = 0
        self.arr = [-1] * self.size 
        self.start = 0
        self.end = 0

    def insert_front(self, value: int) -> bool:
        if self.is_full():
            return False
        
        if not self.is_empty():
            self.start = (self.start + self.size - 1) % self.size 
        self.arr[self.start] = value
        self.count += 1
        return True

    def insert_last(self, value: int) -> bool:
        if self.is_full():
            return False

        if not self.is_empty():
            self.end = (self.end + self.size + 1) % self.size
        self.arr[self.end] = value
        self.count += 1
        return True

    def delete_front(self) -> bool:
        if self.is_empty():
            return False

        self.arr[self.start] = -1
        if self.count > 1:
            self.start = (self.start + self.size + 1) % self.size
        self.count -= 1
        return True

    def delete_last(self) -> bool:
        if self.is_empty():
            return False

        self.arr[self.end] = -1
        if self.count > 1:
            self.end = (self.end + self.size - 1) % self.size
        self.count -= 1
        return True

    def front(self) -> int:
        return -1 if self.is_empty() else self.arr[self.start]

    def rear(self) -> int:
        return -1 if self.is_empty() else self.arr[self.end]

    def is_empty(self) -> bool:
        return self.count == 0

    def is_full(self) -> bool:
        return self.count == self.size 