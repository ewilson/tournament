drop table if exists tournament;
create table tournament (
       id integer primary key autoincrement,
       start_date text not null,
       tourn_type text not null
);

