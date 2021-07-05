from queue import PriorityQueue

class PriorityQueueImpl:

    def addToPriorityQueue(self):

        pq = PriorityQueue()
        pq.put(1)
        pq.put(10)
        pq.put(5)

        while not pq.empty():
            print(pq.get())

        pq1 = PriorityQueue()
        pq1.put((1, 'one'))
        pq1.put((10, 'ten'))
        pq1.put((5,'five'))
        pq1.put((-1, 'six'))

        while not pq1.empty():
            print(pq1.get())


# class Skill:
#
#     def __init__(self, priority, description):
#         self.priority = priority
#         self.description = description
#         print('New Level:', description)
#         # return
#
#     def __cmp__(self, other):
#         return self.__cmp__(self.priority, other.priority)
#
# q = PriorityQueue()
#
# q.put(Skill(5, 'Proficient'))
# q.put(Skill(10, 'Expert'))
# q.put(Skill(1, 'Novice'))
#
# while not q.empty():
#     next_level = q.get()
#     print 'Processing level:', next_level.description



pq = PriorityQueueImpl()
pq.addToPriorityQueue()