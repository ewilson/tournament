import numpy as np

def round_robin(teams):
    n = len(teams)
    g = Graph(n)
    schedule = []
    while not g.finished():
        at_minimum = g.at_minimum(0)
        if len(at_minimum) > 1:
            first = at_minimum[0]
            for option in at_minimum[1:]:
                if g.is_not_edge(first,option):
                    g.add_edge(first,option)
                    schedule.append(set([teams[first],teams[option]]))
                    break
        else:
            at_next = g.at_minimum(1)
            if len(at_next) > 1:
                print at_next
                first = at_minimum[0]
                for option in at_next:
                    if g.is_not_edge(first,option):
                        g.add_edge(first,option)
                        schedule.append(set([teams[first],teams[option]]))
                        break
    return schedule
                             
class Graph(object):
    def __init__(self,n):
        self.n = n
        self.a = np.zeros(shape=(n,n))
        self.num_edges = self.a.sum(axis=0)
        self.min_edges = 0

    def is_not_edge(self,x,y):
        return self.a[x][y] == 0 

    def add_edge(self,x,y):
        self.a[x][y] = 1
        self.a[y][x] = 1
        self.num_edges = self.a.sum(axis=0)
        self.min_edges = min(self.num_edges)
    
    def at_minimum(self,level):
        return np.where(self.num_edges == self.min_edges + level)[0]

    def finished(self):
        return self.min_edges == (self.n - 1)
        
        
            
            
        
    
    
