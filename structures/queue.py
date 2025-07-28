import threading
import time
from collections import deque


class Queue:
    # FIFO
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


def produce_order(queue, data):
    for item in data:
        queue.enqueue(item)
        time.sleep(0.5)


def consume_order(queue):
    while True:
        time.sleep(2)
        if not queue.is_empty():
            item = queue.dequeue()
            print(item)


if __name__ == "__main__":
    q = Queue()

    t1 = threading.Thread(
        target=produce_order,
        args=(q, ["pizza", "samosa", "pasta", "biryani", "burger"]),
    )
    t2 = threading.Thread(target=consume_order, args=(q,))

    t1.start()
    print("t1 started")

    time.sleep(1)

    t2.start()
    print("t2 started")

    t1.join()
