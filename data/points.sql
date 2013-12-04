select sum(a.score) points
from attempt a, match m
where a.match_id = m.id
and m.tournament_id = 2
and a.player_id = 5
group by a.player_id
;

select p.fname,a.score, m.id
from attempt a, match m, player p
where a.match_id = m.id
and m.tournament_id = 2
and p.id = a.player_id
;

select sum (a.score) points_against
from attempt a, match m
where a.match_id = m.id
and m.tournament_id = 2
and a.player_id != 4
and m.id in (
select m.id from match m, attempt a
where a.player_id = 4
and a.match_id = m.id
and m.tournament_id = 2
);
