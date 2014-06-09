import app.scheduler as scheduler


def test_four_teams_scheduled():
    teams = ['alpha', 'bravo', 'charlie', 'delta']

    schedule = scheduler.round_robin(teams)

    assert len(schedule) == 6
    assert schedule[0] == {'alpha', 'bravo'}
    assert schedule[1] == {'charlie', 'delta'}
    assert schedule[2] == {'alpha', 'charlie'}
    assert schedule[3] == {'delta', 'bravo'}
    assert schedule[4] == {'alpha', 'delta'}
    assert schedule[5] == {'charlie', 'bravo'}


def test_three_teams_scheduled():
    teams = ['alpha', 'bravo', 'charlie']

    schedule = scheduler.round_robin(teams)

    assert len(schedule) == 3
    assert schedule[0] == {'alpha', 'bravo'}
    assert schedule[1] == {'charlie', 'alpha'}
    assert schedule[2] == {'bravo', 'charlie'}


def test_six_teams_scheduled():
    teams = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot']

    schedule = scheduler.round_robin(teams)

    assert len(schedule) == 15


def test_seven_teams_scheduled():
    teams = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf']

    schedule = scheduler.round_robin(teams)

    assert len(schedule) == 21


def test_two_teams_scheduled():
    teams = ['alpha', 'bravo']

    schedule = scheduler.round_robin(teams)

    assert len(schedule) == 1
    assert schedule[0] == {'alpha', 'bravo'}


def test_four_team_bracket():
    entries = ['alpha', 'beta', 'gamma', 'delta']

    schedule = scheduler.bracket(entries)

    assert len(schedule) == 2
    match1 = schedule[0]
    match2 = schedule[1]
    assert match1 == (
        {'player': 'alpha', 'seed': 0},
        {'player': 'delta', 'seed': 3}
    )
    assert match2 == (
        {'player': 'beta', 'seed': 1},
        {'player': 'gamma', 'seed': 2}
    )


def test_six_team_bracket():
    entries = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot']

    schedule = scheduler.bracket(entries)

    assert len(schedule) == 4
    match1 = schedule[0]
    match2 = schedule[1]
    match3 = schedule[2]
    match4 = schedule[3]
    assert match1 == (
        {'player': 'alpha', 'seed': 0},
    )
    assert match2 == (
        {'player': 'bravo', 'seed': 1},
    )
    assert match3 == (
        {'player': 'charlie', 'seed': 2},
        {'player': 'foxtrot', 'seed': 5}
    )
    assert match4 == (
        {'player': 'delta', 'seed': 3},
        {'player': 'echo', 'seed': 4}
    )
