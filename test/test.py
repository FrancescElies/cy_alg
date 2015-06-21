import nose
import cython_algos


def test_queue_01():
    Queue = cython_algos.Queue
    q = Queue()
    nose.tools.assert_is_instance(q, cython_algos.Queue)
