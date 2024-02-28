#! /usr/bin/env python3

import unittest
from queue_tests import QueueTests
from LinkedQueue import LinkedQueue
from ListQueue import ListQueueSimple


def _test(queue_class):
    class QueueTestCase(unittest.TestCase, QueueTests):
        Queue = queue_class

    return QueueTestCase


TestLinkedQueue = _test(ListQueueSimple)
TestListQueue = _test(LinkedQueue)

if __name__ == "__main__":
    unittest.main()
