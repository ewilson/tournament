import numpy as np

class RoundRobinBuilder(object):
    def __init__(self, teams):
        self.teams = teams

        self.schedule = []
def round_robin(teams):
    g = Graph(len(teams))
    schedule = []

    def _choose_pair(first, options):
        for option in options:
            if g.is_not_edge(first,option):
                g.add_edge(first,option)
                schedule.append(set([teams[first],teams[option]]))
                break

    while not g.finished():
        options = list(g.at_minimum(0))
        next_options = g.at_minimum(1)
        options.extend(next_options)
        _choose_pair(options[0],options[1:])
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
        
