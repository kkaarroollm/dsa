"""
Big O:
- insert: O(log n)
- extract: O(log n)
- size: O(1)
- peek: O(1)
"""

from functools import total_ordering

@total_ordering
class Task:
    def __init__(self, name: str, priority: int):
        self.name = name
        self.priority = priority

    def __lt__(self, other: "Task"):
        return self.priority < other.priority

    def __repr__(self):
        return f"Task({self.name}, {self.priority})"


class PriorityQueue:
    # max prio on top
    def __init__(self):
        self.__heap: list["Task"] = []
        self.__size = 0

    @property
    def size(self) -> int:
        return self.__size

    @property
    def peek(self) -> Task:
        return self.__heap[0]

    def is_empty(self) -> bool:
        return self.__size == 0

    def insert(self, task: Task):
        self.__heap.append(task)
        self.__size += 1
        self.__heapify_up()

    def extract(self) -> Task:
        r = self.__heap.pop(0)
        self.__size -= 1
        self.__heapify_down()
        return r

    def __heapify_up(self):
        idx = self.__size - 1
        while idx > 0:
            parent = (idx - 1) // 2
            if self.__heap[idx] <= self.__heap[parent]:
                break
            self.__heap[idx], self.__heap[parent] = self.__heap[parent], self.__heap[idx]
            idx = parent

    def __heapify_down(self):
        idx = 0
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            largest = idx

            if left < self.__size and self.__heap[left] > self.__heap[largest]:
                largest = left
            if right < self.__size and self.__heap[right] > self.__heap[largest]:
                largest = right

            if largest == idx:
                break

            self.__heap[idx], self.__heap[largest] = self.__heap[largest], self.__heap[idx]
            idx = largest


pq = PriorityQueue()

pq.insert(Task("eat something", 3))
pq.insert(Task("brush teeth", 5))
pq.insert(Task("clean the dishes", 1))
pq.insert(Task("drink coffee", 4))
pq.insert(Task("check mails", 2))

# top_tier_task = pq.extract()

for _ in range(pq.size):
    print(pq.extract())
    # print(pq._PriorityQueue__heap)

