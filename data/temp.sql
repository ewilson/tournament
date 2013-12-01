select player_id,
       sum(result='W') win,
       sum(result='L') loss,
       sum(result='T') tie from
(
  select a.player_id,
  case when a.score = ss.winscore and a.score > ss.losescore
       then 'W'
       else case when a.score = ss.losescore and a.score < ss.winscore
	         then 'L'
		 else 'T'
            	 end
     	    end as result
  from attempt a
  inner join (
    select a.match_id, max(a.score) winscore, min(a.score) losescore 
    from attempt a, match m
    where a.match_id = m.id
    and m.tournament_id = 27
    and m.entered_time is not null
    group by a.match_id
  ) ss on a.match_id = ss.match_id
) group by player_id
order by win 
desc
;
