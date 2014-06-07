from flask import g

from models import Standing


def find(tournament_id):
    select = """
    select pid, fname,
       sum(result='W') win,
       sum(result='L') loss,
       sum(result='T') tie,
       sum(score) pts,
       sum(opp_score) pts_agst
    from (
        select p.id pid, p.fname, a.score, a.opp_score,
        case when a.score > a.opp_score
         then 'W'
         else case when a.score < a.opp_score
              then 'L'
          else case when m.entered_time is not null
               then 'T'
               else ''
          end
         end
    end as result
    from attempt a, player p, match m
    where a.player_id = p.id
    and a.match_id = m.id
        and m.tournament_id = ?
    ) group by pid
    """
    cur = g.db.execute(select, [tournament_id])
    return [Standing(*row) for row in cur.fetchall()]

