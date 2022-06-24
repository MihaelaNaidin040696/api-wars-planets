create table planet_votes
(
    id              serial
        constraint planet_votes_pk
            primary key,
    planet_name     varchar,
    submission_time date default now(),
    planet_id       integer,
    user_id         integer
);

create unique index planet_votes_id_uindex
    on planet_votes (id);


