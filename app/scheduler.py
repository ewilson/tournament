import math

import numpy as np


def bracket(teams):
    schedule = []
    num_teams = len(teams)
    num_rounds = math.ceil(np.log2(num_teams))
    bracket_size = int(2 ** num_rounds)
    for n in range(bracket_size / 2):
        comp = bracket_size - n - 1
        player1 = {'player': teams[n], 'seed': n}
        if comp < num_teams:
            schedule.append((player1, {'player': teams[comp], 'seed': comp}))
        else: # player1 gets a bye
            schedule.append((player1,))
    return schedule


def round_robin(teams):
    g = Graph(len(teams))
    schedule = []

    def _choose_pair(first, options):
        for option in options:
            if g.is_not_edge(first, option):
                g.add_edge(first, option)
                schedule.append({teams[first], teams[option]})
                break

    while not g.finished():
        options = list(g.at_minimum(0))
        next_options = g.at_minimum(1)
        options.extend(next_options)
        _choose_pair(options[0], options[1:])
    return schedule


class Graph(object):
    def __init__(self, n):
        self.n = n
        self.a = np.zeros(shape=(n, n))
        self.num_edges = self.a.sum(axis=0)
        self.min_edges = 0

    def is_not_edge(self, x, y):
        return self.a[x][y] == 0

    def add_edge(self, x, y):
        self.a[x][y] = 1
        self.a[y][x] = 1
        self.num_edges = self.a.sum(axis=0)
        self.min_edges = min(self.num_edges)

    def at_minimum(self, level):
        return np.where(self.num_edges == self.min_edges + level)[0]

    def finished(self):
        return self.min_edges == (self.n - 1)

