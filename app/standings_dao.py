from flask import g
import sqlite3
from models import Standing

def find(tournament_id):
    select = """
    select fname,
	   sum(result='W') win,
	   sum(result='L') loss,
	   sum(result='T') tie from
    (
      select p.fname, a.player_id,
      case when a.score = ss.winscore and a.score > ss.losescore
	   then 'W'
	   else case when a.score = ss.losescore and a.score < ss.winscore
		     then 'L'
		     else case when entered_time is not null
		     	       then 'T'
			       else ''
			  end
		     end
		end as result
      from player p, attempt a
      inner join (
	select a.match_id, 
	       max(a.score) winscore, 
	       min(a.score) losescore,
	       m.entered_time
	from attempt a, match m
	where a.match_id = m.id
	and m.tournament_id = ?
	group by a.match_id
      ) ss on a.match_id = ss.match_id and p.id = a.player_id
    ) group by player_id
    order by win desc
    """
    cur = g.db.execute(select, [tournament_id])
    return [Standing(*row) for row in cur.fetchall()]
