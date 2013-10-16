class Tournament:
    def __init__(self, id, start_date, tourn_type, description, begun):
        self.id = id
        self.start_date = start_date
        self.tourn_type = tourn_type
        self.description = description
        self.begun = begun
    
    def __repr__(self):
        return ('<(%d)%s:%s--%s>' % 
                (self.id, self.description, self.tourn_type, self.start_date))
