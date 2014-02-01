drop table if exists tournament;
create table tournament (
       id integer primary key autoincrement,
       start_date text not null,
       description text not null,
       tourn_type text not null,
       status integer not null
);

drop table if exists match;
create table match (
       id integer primary key autoincrement,
       tournament_id integer not null,
       entered_time text,
       foreign key (tournament_id) references tournament (id) on delete cascade
);

drop table if exists player;
create table player (
       id integer primary key autoincrement,
       fname text unique not null
);

-- "attempt" could be called player_match
drop table if exists attempt;
create table attempt (
       player_id integer not null,
       match_id integer not null,
       score integer,
       opp_score integer,
       primary key (player_id, match_id),
       foreign key (player_id) references player (id),
       foreign key (match_id) references match (id) on delete cascade
);

-- "entry" could be called player_tournament
drop table if exists entry;
create table entry (
       player_id integer not null,
       tournament_id integer not null,
       champion integer,
       primary key (player_id, tournament_id),
       foreign key (player_id) references player (id),
       foreign key (tournament_id) references tournament (id) on delete cascade
);

