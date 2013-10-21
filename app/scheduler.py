import numpy as np

def round_robin(teams):
    builder = RoundRobinBuilder(teams)
    return builder.build_round_robin()

class RoundRobinBuilder(object):
    def __init__(self, teams):
        self.teams = teams
        self.g = Graph(len(teams))
        self.schedule = []

    def build_round_robin(self):
        while not self.g.finished():
            at_minimum = self.g.at_minimum(0)
            print at_minimum
            first = at_minimum[0]
            if len(at_minimum) > 1:
                self._choose_pair(first, at_minimum[1:])
            else:
                at_next = self.g.at_minimum(1)
                if len(at_next) > 1:
                    self._choose_pair(first, at_next)
        return self.schedule

    def _choose_pair(self, first, options):
        for option in options:
            if self.g.is_not_edge(first,option):
                self.g.add_edge(first,option)
                self.schedule.append(set([self.teams[first],self.teams[option]]))
                break
            
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
        
