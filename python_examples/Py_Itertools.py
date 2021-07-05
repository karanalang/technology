# https://medium.com/@jasonrigden/a-guide-to-python-itertools-82e5a306cdf8
import itertools
import operator

class Python_Itertools:

    def usingItertools_accumulate(self):
        data = [1, 2, 3, 4, 5]

        result = itertools.accumulate(data)
        print(result)
        for res in result:
            print(" itertools.accumulate(data), adds subsequent values -> ", res)

        result2 = itertools.accumulate(data, operator.mul)
        for res in result2:
            print(" itertools.accumulate(data, operator.mul) -> ", res)

        data1 = [5, 2, 6, 4, 5, 9, 1]
        maxResult = itertools.accumulate(data1, max)
        for res in maxResult:
            print(" res -> ", res)

    def usingItertools_combinations(self):

        shapes = ['circle', 'square', 'triangle', 'quadrilateral']
        res = itertools.combinations(shapes, 3)

        # for r in res:
        #     print(" results -> ", r)


        res_with_replacement = itertools.combinations_with_replacement(shapes, 2)
        for res in res_with_replacement:
            print(" res -> ", res)

    def usingItertools_count(self):

        res1 = itertools.count(10, 3)
        print(" res1 -> ", res1)
        for i in res1:
            if i >= 20:
                break
            else:
                print('i -> ', i)

    def usingItertools_cycle(self):

        l = ['red', 'yellow', 'orange', 'green', 'blue', 'white']

        res = itertools.cycle(l)
        for r in res:
            print(" r -> ", r)

    def usingItertools_chain(self):

        colors = ['red', 'blue', 'green']
        shapes = ['circle', 'triangle', 'square', 'pentagon']

        res = itertools.chain(colors, shapes)
        print(" result of itertools.chain -> ", res)

        for r in res:
            print(' itertools.chain, r -> ', r)

    def usingItertools_compress(self):

        shapes = ['circle', 'triangle', 'square', 'pentagon']
        selections = [True, True, True, True]

        res = itertools.compress(shapes, selections)
        for r in res:
            print(" r -> ", r)

    def usingItertools_dropwhile(self):

        data = [1, 2, 3, 4, 7, 9, 57, 1, 9]
        res = itertools.dropwhile(lambda x: x < 5, data)

        for r in res:
            print(" dropped x < 5 -> ", r)

    def usingItertools_filterfalse(self):

        data = [1, 2, 3, 4, 5, 8, 10, 0]
        res = itertools.filterfalse(lambda x: x<5, data)
        for r in res :
            print(" filterFalse, r -> ", r)

    def usingItertools_groupby(self):

        robots = [{
            'name': 'blaster',
            'faction': 'autobot'
        }, {
            'name': 'galvatron',
            'faction': 'decepticon'
        }, {
            'name': 'jazz',
            'faction': 'autobot'
        }, {
            'name': 'metroplex',
            'faction': 'autobot'
        }, {
            'name': 'megatron',
            'faction': 'decepticon'
        }, {
            'name': 'starcream',
            'faction': 'decepticon'
        }]

        for key, group in itertools.groupby(robots, key=lambda x: x['faction']):
            print(key)
            print(list(group))

    def usingItertools_isslice(self):

        colors = ['red','blue','green','yellow', 'white', 'purple', 'magenta']
        few_colors = itertools.islice(colors, 0, 7, 2)

        for color in few_colors:
            print(" itertools.isslice, color -> ", color)

    def usingItertools_permutations(self):

        data = [1, 5, 3]
        res = itertools.permutations(data)
        for permutation in res:
            print(" permutation -> ", permutation)


    def usingItertools_product(self):

        # creates cartesian product
        num_data = [1, 2, 3]
        alpha_data = ['a', 'b', 'c']
        res = itertools.product(num_data, alpha_data)
        for r in res:
            print(' itertools.product creates cartesian product -> ', r)

    def usingItertools_repeat(self):

        for res in itertools.repeat('spam', 10):
            print(" res -> ", res)


    def usingItertools_starmap(self):

        data = [(2,6), (8,4), (7,3)]
        result = itertools.starmap(operator.mul, data)

        for res in result:
            print(' itertool.starmap res ->', res)

    def usingItertools_takewhile(self):

        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
        result = itertools.takewhile(lambda x : x < 5, data)
        for r in result:
            print(" using itertools.takewhile, r -> ", r)

    def usingItertools_tee(self):

        colors = ['red', 'blue', 'green', 'yellow']
        alpha_colors, beta_colors, gama_colors = itertools.tee(colors, 3)

        for alpha in alpha_colors:
            print(' alpha -> ', alpha)

        for beta in beta_colors:
            print(' beta -> ', beta)

        for gama in gama_colors:
            print(' gama -> ', gama)

    def usingItertools_ziplongest(self):

        colors = ['red', 'blue', 'green', 'yellow']
        data = [1, 2, 3, 4, 5, 6, 1, 4, 2, 3, 5]

        res = itertools.zip_longest(colors, data, fillvalue=None)
        for i in res:
            print(' using zipLongest -> ', i)



sol = Python_Itertools()
sol.usingItertools_accumulate()
# sol.usingItertools_combinations()
# sol.usingItertools_count()
# sol.usingItertools_cycle()
# sol.usingItertools_chain()
# sol.usingItertools_compress()
# sol.usingItertools_dropwhile()
# sol.usingItertools_filterfalse()
# sol.usingItertools_groupby()
# sol.usingItertools_isslice()
# sol.usingItertools_permutations()
# sol.usingItertools_product()
# sol.usingItertools_repeat()
# sol.usingItertools_starmap()
# sol.usingItertools_takewhile()
# sol.usingItertools_tee()
# sol.usingItertools_ziplongest()