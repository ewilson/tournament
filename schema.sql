drop table if exists tournament;
create table tournament (
       id integer primary key autoincrement,
       start_date text not null,
       description text not null,
       tourn_type text not null,
       begun integer not null
);
drop table if exists matches;
create table matches (
       id integer primary key autoincrement,
       tournament_id integer not null,
       entered_time text not null,
       player_1_id integer not null,
       player_2_id integer not null,
       player_1_score integer,
       player_2_score integer,
       completed integer not null
);

