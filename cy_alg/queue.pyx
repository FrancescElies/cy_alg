# Based on http://docs.cython.org/src/tutorial/clibraries.html

cimport cqueue

cdef class Queue:
    cdef cqueue.Queue * _c_queue

    def __cinit__(self):
        self._c_queue = cqueue.queue_new()
        if self._c_queue is NULL:
            raise MemoryError()

    def __dealloc__(self):
        if self._c_queue is not NULL:
            cqueue.queue_free(self._c_queue)

    cpdef append(self, pyobj):
        cdef void *ptr
        ptr = <void *>pyobj
        if not cqueue.queue_push_tail(self._c_queue, ptr):
            raise MemoryError()
