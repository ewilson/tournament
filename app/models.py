class Tournament(object):
    def __init__(self, tournament_id=0, start_date='', description='',
                 tourn_type='', status=0):
        self.tournament_id = tournament_id
        self.start_date = start_date
        self.tourn_type = tourn_type
        self.description = description
        self.status = int(status)

    def __repr__(self):
        return ('<(%d)%s:%s--%s, status=%s>' %
                (self.tournament_id, self.description,
                 self.tourn_type, self.start_date, self.status))


class Player(object):
    def __init__(self, fname='', id=0):
        self.id = id
        self.fname = fname

    def __str__(self):
        return '<(%d)%s>' % (self.id, self.fname)


class Match(object):
    def __init__(self, player1=None, player2=None, score1=0, score2=0, match_id=0):
        self.match_id = match_id
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2

    def __repr__(self):
        return '<(%d): %s vs %s>' % (self.match_id, self.player1, self.player2)


class Standing(object):
    def __init__(self, pid=0, name=0, win=0, loss=0, tie=0, pf=0, pa=0):
        self.pid = pid
        self.name = name
        self.win = win
        self.loss = loss
        self.tie = tie
        self.pf = pf if isinstance(pf, (int, float)) else 0
        self.pa = pa if isinstance(pa, (int, float)) else 0
        self.perc = self.compute_percent()
        self.percent_display = "%.1f" % self.perc

    def compute_percent(self):
        games = self.win + self.loss + self.tie
        if games == 0:
            p = 0.0
        else:
            p = 100.0 * (self.win + 0.5 * self.tie) / games
        return p

    def __repr__(self):
        return '(%d)--%s-- W: %d, L: %d' % (self.pid, self.name, self.win, self.loss)

