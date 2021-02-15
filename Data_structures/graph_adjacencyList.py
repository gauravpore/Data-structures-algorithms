#Graph implementation (AdjacencyS list)

class Graph:
    def __init__(self,nodes):
        self.nodes = nodes
        self.adj_list= {} #empty dict initialized

        for node in nodes:
            self.adj_list[node]=[]

    def add_edge(self,vertex,edge):
        self.adj_list[vertex].append(edge)
        self.adj_list[edge].append(vertex) #non-directional graph

    def get_degree(self,vertex):
        return "{}'s degree:{}".format(vertex,len(self.adj_list[vertex]))

    def print_adj(self):
        for node in nodes:
            print (node,":",self.adj_list[node])

nodes = ["A","B","C","D","E"]
edges = [("A","B"),('A','C'),('B','C'),('B','D'),('B','E'),('C','D'),('D','E')]
g = Graph(nodes)
for v,e in edges:
  g.add_edge(v,e)
g.print_adj()
print (g.get_degree('C'))









