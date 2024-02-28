#! /usr/bin/env python3

import unittest
from ListQueue import ListQueueSimple


class TestListQueue(unittest.TestCase):
    def test_init(self) -> None:
        q = ListQueueSimple

    def test_add_and_remove_one_item(self) -> None:
        q = ListQueueSimple()
        q.enqueue(3)
        self.assertEqual(q.dequeue(), 3)

    def test_alternativ_add_remove(self) -> None:
        q = ListQueueSimple()
        for i in range(1000):
            q.enqueue(i)
            self.assertEqual(q.dequeue(), i)

    def test_many_operations(self) -> None:
        q = ListQueueSimple()
        for i in range(1000):
            q.enqueue(2 * i + 3)
        for i in range(1000):
            self.assertEqual(q.dequeue(), 2 * i + 3)

    def test_length(self) -> None:
        q = ListQueueSimple()
        self.assertEqual(len(q), 0)

        for i in range(10):
            q.enqueue(i)
        self.assertEqual(len(q), 10)

        for i in range(10):
            q.enqueue(i)
        self.assertEqual(len(q), 20)

        for i in range(15):
            q.dequeue()
        self.assertEqual(len(q), 5)


if __name__ == "__main__":
    unittest.main()
