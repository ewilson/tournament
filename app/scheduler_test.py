import scheduler

def test_four_teams_scheduled():
    teams = ['alpha','bravo','charlie','delta']

    schedule = scheduler.round_robin(teams)

    assert len(schedule) == 6
    assert schedule[0] == set(['alpha','bravo'])
    assert schedule[1] == set(['charlie','delta'])
    assert schedule[2] == set(['alpha','charlie'])
    assert schedule[3] == set(['delta','bravo'])
    assert schedule[4] == set(['alpha','delta'])
    assert schedule[5] == set(['charlie','bravo'])

def test_three_teams_scheduled():
    teams = ['alpha','bravo','charlie']

    schedule = scheduler.round_robin(teams)

    assert len(schedule) == 3
    assert schedule[0] == set(['alpha','bravo'])
    assert schedule[1] == set(['charlie','alpha'])
    assert schedule[2] == set(['bravo','charlie'])

def test_six_teams_scheduled():
    teams = ['alpha','bravo','charlie','delta','echo','foxtrot']

    schedule = scheduler.round_robin(teams)

    assert len(schedule) == 15

def test_seven_teams_scheduled():
    teams = ['alpha','bravo','charlie','delta','echo','foxtrot','golf']

    schedule = scheduler.round_robin(teams)

    assert len(schedule) == 21

def test_two_teams_scheduled():
    teams = ['alpha','bravo']

    schedule = scheduler.round_robin(teams)

    assert len(schedule) == 1
    assert schedule[0] == set(['alpha','bravo'])
