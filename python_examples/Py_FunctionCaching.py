from functools import lru_cache

class Py_Function_Caching:

    @lru_cache(maxsize=32)
    def fib(self, n):

        if n < 2 :
            return n

        # t uncache

        return self.fib(n-1) + self.fib(n-2)


funcCache = Py_Function_Caching()
# fibNo = funcCache.fib(46)
# print(" fibNo -> ", fibNo)

print(" fib numbers ->", [funcCache.fib(n) for n in range(5)])


# funcCache.cache_clear()