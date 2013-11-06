drop table if exists tournament;
create table tournament (
       id integer primary key autoincrement,
       start_date text not null,
       description text not null,
       tourn_type text not null,
       begun integer not null
);

drop table if exists match;
create table match (
       id integer primary key autoincrement,
       tournament_id integer not null,
       entered_time text
);

drop table if exists player;
create table player (
       id integer primary key autoincrement,
       fname text not null
);

-- "attempt" could be called player_match
drop table if exists attempt;
create table attempt (
       player_id integer not null,
       match_id integer not null,
       score integer
);

-- "entry" could be called player_tournament
drop table if exists entry;
create table entry (
       player_id integer not null,
       tournament_id integer not null,
       champion integer
);

