from typing import List

class SegmentTree:
    def __init__(self, arr: List[int]):
        self.size = 1
        while self.size < len(arr):
            self.size *= 2
        self.arr = [0] * (2 * self.size)
        self._build(arr, 0, 0, self.size)

    def update(self, i: int, val: int) -> None:
        self._update(i, val, 0, 0, self.size)

    def query(self, l: int, r: int) -> int:
        return self._query(l, r, 0, 0, self.size)

    def _build(self, arr: List[int], x: int, lx: int, rx: int) -> None:
        if rx - lx == 1:
            if lx < len(arr):
                self.arr[x] = arr[lx]
            return

        mid = (lx + rx) // 2
        self._build(arr, x * 2 + 1, lx, mid)
        self._build(arr, x * 2 + 2, mid, rx)

        self.arr[x] = self.arr[x * 2 + 1] + self.arr[x * 2 + 2]

    def _update(self, i: int, val: int, x: int, lx: int, rx: int) -> None:
        if rx - lx == 1:
            self.arr[x] = val
            return
        
        mid = (lx + rx) // 2
        if i < mid:
            self._update(i, val, x * 2 + 1, lx, mid)
        else:
            self._update(i, val, x * 2 + 2, mid, rx)

        self.arr[x] = self.arr[x * 2 + 1] + self.arr[x * 2 + 2]

    def _query(self, l: int, r: int, x: int, lx: int, rx: int) -> int:
        if rx <= l or r <= lx:
            return 0
        if l <= lx and rx <= r:
            return self.arr[x]
        
        mid = (lx + rx) // 2
        res1 = self._query(l, r, x * 2 + 1, lx, mid)
        res2 = self._query(l, r, x * 2 + 2, mid, rx)

        return res1 + res2