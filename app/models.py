class Tournament(object):
    def __init__(self, id, start_date, description, tourn_type, begun):
        self.id = id
        self.start_date = start_date
        self.tourn_type = tourn_type
        self.description = description
        self.begun = int(begun)
    
    def __repr__(self):
        return ('<(%d)%s:%s--%s, begun=%s>' % 
                (self.id, self.description, 
                 self.tourn_type, self.start_date,self.begun))

class Player(object):
    def __init__(self, fname, id = 0):
        self.id = id
        self.fname = fname
    
    def __repr__(self):
        return '<(%d)%s>' % (self.id, self.fname)

class Match(object):
    def __init__(self, player1=None, player2=None, id = 0):
        self.id = id
        self.player1 = player1
        self.player2 = player2

    def __repr__(self):
        return '<(%d): %s vs %s>' % (self.id, self.player1, self.player2)

