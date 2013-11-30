select player_id, sum(result='W') wins, sum(result='L') losses from 
(
  select a.player_id,
  case when a.score = ss.winscore then 'W' else 'L' end as result
  from attempt a
  inner join (
    select match_id, max(score) winscore, min(score) losescore from attempt 
    where match_id >= 48
    group by match_id
  ) ss on a.match_id = ss.match_id
) group by player_id
order by wins desc
;
