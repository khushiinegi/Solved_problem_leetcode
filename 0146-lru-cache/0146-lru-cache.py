class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes
        self.left = Node()   # Least recently used side
        self.right = Node()  # Most recently used side

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        """Remove a node from the doubly linked list."""
        previous_node = node.prev
        next_node = node.next

        previous_node.next = next_node
        next_node.prev = previous_node

    def insert(self, node):
        """Insert a node before right (most recently used position)."""
        previous_node = self.right.prev

        previous_node.next = node
        node.prev = previous_node

        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Move accessed node to most recently used position
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove the old node
            self.remove(self.cache[key])

        # Create and insert the new node
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)

        # Remove least recently used node if capacity is exceeded
        if len(self.cache) > self.capacity:
            lru_node = self.left.next

            self.remove(lru_node)
            del self.cache[lru_node.key]