class Tournament:
    def __init__(self, start_date, tourn_type, description):
        self.start_date = start_date
        self.tourn_type = tourn_type
        self.description = description
    
    def __repr__(self):
        return '<%s:%s--%s>' % (self.description, self.tourn_type, self.start_date)
