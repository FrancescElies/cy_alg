import nose
import cython_algos as cya


def test_queue_01():
    """test_queue_01: create queue
    """
    q = cya.Queue()
    nose.tools.assert_is_instance(q, cya.Queue)


def test_queue_02():
    """test_queue_02: memory management
    """
    q = cya.Queue()
    del q
