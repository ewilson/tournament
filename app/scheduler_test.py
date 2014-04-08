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

def test_four_team_bracket():
    entries = ['alpha','beta','gamma','delta']

    schedule = scheduler.bracket(entries)

    assert len(schedule) == 2
    match1 = schedule[0]
    match2 = schedule[1]
    assert match1[0]['player'] == 'alpha'
    assert match1[0]['seed'] == 0
    assert match1[1]['player'] == 'delta'
    assert match1[1]['seed'] == 3
    assert match2[0]['player'] == 'beta'
    assert match2[0]['seed'] == 1
    assert match2[1]['player'] == 'gamma'
    assert match2[1]['seed'] == 2

def test_six_team_bracket():
    entries = ['alpha','bravo','charlie','delta','echo','foxtrot']

    schedule = scheduler.bracket(entries)

    assert len(schedule) == 4
    match1 = schedule[0]
    match2 = schedule[1]
    match3 = schedule[2]
    match4 = schedule[3]
    assert match1[0]['player'] == 'alpha'
    assert match1[0]['seed'] == 0
    assert len(match1) == 1
    assert match2[0]['player'] == 'bravo'
    assert match2[0]['seed'] == 1
    assert len(match2) == 1
    assert match3[0]['player'] == 'charlie'
    assert match3[0]['seed'] == 2
    assert match3[1]['player'] == 'foxtrot'
    assert match3[1]['seed'] == 5
    assert len(match3) == 2
    assert match4[0]['player'] == 'delta'
    assert match4[0]['seed'] == 3
    assert match4[1]['player'] == 'echo'
    assert match4[1]['seed'] == 4
    assert len(match4) == 2
