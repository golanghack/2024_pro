#! /usr/bin/env python3

"""DRY

This class with tests are an universaly for any queue
"""


class QueueTests:
    def test_init(self):
        queue = self.Queue()

    def test_add_and_remove_one_item(self):
        queue = self.Queue()
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 3)

    def test_alternative_add_and_remove_item(self):
        queue = self.Queue()
        for i in range(1000):
            queue.enqueue(i)
            self.assertEqual(queue.dequeue(), i)

    def test_many_operations(self):
        queue = self.Queue()
        for i in range(1000):
            queue.enqueue(2 * i + 3)
        for i in range(1000):
            self.assertEqual(q.dequeue(), 2 * i + 3)

    def test_lenght(self):
        queue = self.Queue()
        self.assertEqual(len(queue), 0)
        for i in range(10):
            queue.enqueue(i)
        self.assertEqual(len(queue), 10)
        for i in range(10):
            queue.enqueue(i)
        self.assertEqual(len(queue), 20)
        for i in range(15):
            queue.dequeue()
        self.assertEqual(len(queue), 5)
