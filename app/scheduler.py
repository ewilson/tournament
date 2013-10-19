import numpy as np

def foo(num):
    return num + num

def round_robin(teams):
    n = len(teams)
    a = np.zeros(shape=(n,n))
    b = a.sum(axis=0)
    schedule = []
    fewest_games = min(b)
    while fewest_games < (n-1):
        at_minimum = np.where(b == fewest_games)[0]
        if len(at_minimum) > 1:
            first = at_minimum[0]
            for option in at_minimum[1:]:
                if a[first][option] == 0:
                    a[first][option] = 1
                    a[option][first] = 1
                    b = a.sum(axis=0)
                    schedule.append(set([teams[first],teams[option]]))
                    break
        else:
            print 'oh oh'
        fewest_games = min(b)
    return schedule
                             
            
            
            
        
    
    
