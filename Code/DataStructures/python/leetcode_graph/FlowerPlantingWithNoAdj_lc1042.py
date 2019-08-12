from typing import List
from collections import defaultdict

class FlowerPlantingWithNoAdj:

    def gardenNoAdj(self, N, paths: List[List[int]]):

        # N - number of gardens
        # paths - shows the links between the gardens
        #

        g = defaultdict(list)
        print(" g - defaultdict -> ", g)
        for x, y in paths:
            print(" x -> ", x, " y -> ", y)
            g[x].append(y)
            g[y].append(x)

        print(" g ->  ", g)

        # We create a plantdict so we know which flower
        # we're planting in each garden. We go through all the gardens and plant a flower. ' \
        # 'Everytime we plant a flower, we update our plantdict so that gardens that are connected will not plant the same flower.
        plantdict = {i:0 for i in range(1, N+1)}
        print(" plantdict -> ", plantdict)

        for garden in g:
            print(" garden in g -> ", garden)
            pick = set(range(1,5))
            print(" pick is -> ", pick)
            for each in g[garden]:
                print(" each is -> ", each, " plantdict[each] -> ", plantdict[each])
                # if(plantdict[each] !=0 and plantdict[each] in pick):
                if (plantdict[each] != 0):
                    print(" removing plantdict[each] -> ", plantdict[each])
                    pick.remove(plantdict[each]) # since this is already allocated to garden - each
                    print(" pick after removing -> ", pick)
            # why is this being done ?
            # now, of the remaining in 'pick', choose one & assign to the garden
            plantdict[garden] = pick.pop() # or pick[len(pick) -1]
            # plantdict[garden] = pick.pop([len(pick) -1])
            print(" 2.plantdict -> ", plantdict, " plantdict[garden] -> ", plantdict[garden])

        return [plantdict[x] if(plantdict[x] !=0) else 1 for x in range(1, N+1)]

        # pass



g = FlowerPlantingWithNoAdj()

paths = [[1,2],[2,3],[3,1]]
ans = g.gardenNoAdj(3, paths)
print(" ans -> ", ans)
