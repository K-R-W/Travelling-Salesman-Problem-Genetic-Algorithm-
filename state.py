from graph import graph
import numpy as np

class state:
    def __init__(self, graph:graph, path):
        self.network = graph
        self.path = path # expect path to contain root index twice, in beginning and end
        self.start = path[0]
        self.path_dist = self.path_distance()

    #operator overload to support hashing so objects can be compared in sets
    def __eq__(self,other):
        return self.path==other.path
    def __hash__(self):
        return hash(tuple(self.path,))
    def __gt__(self,other):
        return (self.path_dist>other.path_dist)

    def __str__(self):
        return str(self.path)+"(cost:{0})".format(self.path_dist)

    def swap_city(self,idx1,idx2):
        self.path[idx1],self.path[idx2]=self.path[idx2],self.path[idx1]
        self.path_dist = self.path_distance()

    def path_distance(self):
        path_distance = 0
        prev = self.path[0]

        for city in self.path[1:]:
            if(city not in self.network.adj_list[prev]):
                return np.inf
            path_distance+=self.network.adj_list[prev][city]
            prev=city
        return path_distance