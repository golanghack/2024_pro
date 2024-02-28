#! /usr/bin/env python3

import unittest
from queue_tests import QueueTests
from ListQueue import ListQueueSimple


class TestListQueue(unittest.TestCase, QueueTests):
    Queue = ListQueueSimple


if __name__ == "__main__":
    unittest.main()
