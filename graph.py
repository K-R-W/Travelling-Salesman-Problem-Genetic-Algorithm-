import numpy as np
class graph:
    def __init__(self,filename):
        self.edge_graph = []
        self.adj_list=[]
        self.V=0
        self.read_file(filename)
        self.adj_list_maker()
    
        self.parent=[]
        self.size=[]

    def read_file(self,filename):
        with open(filename,'r') as f:
            for row in f: 
                edge = [int(x) for x in row.strip().split()]
                self.V=max(self.V,edge[0]+1,edge[1]+1)
                self.edge_graph.append(edge)
            self.edge_graph.sort(key = lambda x:x[2])

    def adj_list_maker(self):
        self.adj_list=[dict() for _ in range(self.V)]
        for row in self.edge_graph:
            self.adj_list[row[0]][row[1]]=row[2]
            self.adj_list[row[1]][row[0]]=row[2]
    
    def neighbours(self,v):
        return self.adj_list[v]

    def addedge(self,s,e,cost):
        self.edge_graph.append([s,e,cost])
    
