class LoopThroughDict:

    def loop(self, d:dict):

        for key in d.keys():
            print(" key -> ", key, " value -> ", d[key])
            if key == "neighbors":
                self.loop(d["neighbors"][0])



l = LoopThroughDict()
d = {"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

l.loop(d)