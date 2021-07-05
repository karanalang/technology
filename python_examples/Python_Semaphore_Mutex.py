# https://www.bogotobogo.com/python/Multithread/python_multithreading_Synchronization_Semaphore_Objects_Thread_Pool.php

import threading
import logging
import time

# logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s',)
logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s',)


class ThreadPool(object):
    def __init__(self):
        super(ThreadPool, self).__init__()
        self.active = []
        self.lock = threading.Lock()


    def makeActive(self, name):
        with self.lock:
            self.active.append(name)
            logging.debug('Running: %s', self.active)

    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)
            logging.debug('Running: %s', self.active)


def f(s, pool):
    logging.debug('Waiting to join the pool')
    with s:
        name = threading.currentThread().getName()
        pool.makeActive(name)
        time.sleep(0.5)
        pool.makeInactive(name)

if __name__ == '__main__':
    pool = ThreadPool()
    s = threading.Semaphore(3)
    for i in range(10):
        t = threading.Thread(target=f, name='thread_'+str(i), args=(s, pool))
        t.start()