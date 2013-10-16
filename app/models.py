class Tournament:
    def __init__(self, id, start_date, tourn_type, description):
        self.id = id
        self.start_date = start_date
        self.tourn_type = tourn_type
        self.description = description
    
    def __repr__(self):
        return ('<(%d)%s:%s--%s>' % 
                (self.id, self.description, self.tourn_type, self.start_date))
