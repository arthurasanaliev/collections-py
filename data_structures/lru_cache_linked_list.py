class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.start = Node(-1, -1)
        self.end = Node(-1, -1)

        self.start.next = self.end
        self.end.prev = self.start

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._delete_node(node)
        self._add_node(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value

            self._delete_node(node)
            self._add_node(node)
        else:
            node = Node(key, value)
            self.cache[key] = node 
            self._add_node(node)
            
            self.cap -= 1
            if self.cap < 0:
                self.cap = 0
                lru_node = self.start.next
                del self.cache[lru_node.key]
                self._delete_node(lru_node)

    def _delete_node(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_node(self, node: Node) -> None:
        last_node = self.end.prev

        last_node.next = node
        node.prev = last_node
        node.next = self.end
        self.end.prev = node