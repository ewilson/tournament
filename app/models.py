class Tournament:
    def __init__(self, id, start_date, tourn_type, description, begun):
        self.id = id
        self.start_date = start_date
        self.tourn_type = tourn_type
        self.description = description
        self.begun = int(begun)
    
    def __repr__(self):
        return ('<(%d)%s:%s--%s, begun=%s>' % 
                (self.id, self.description, 
                 self.tourn_type, self.start_date,self.begun))

class Player:
    def __init__(self, id, fname):
        self.id = id
        self.fname = fname
    
    def __repr__(self):
        return '<(%d)%s>' % (self.id, self.fname)
