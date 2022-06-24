create table user_credentials
(
    id       serial
        constraint user_credentials_pk
            primary key,
    username varchar not null,
    password varchar not null
);

create unique index user_credentials_id_uindex
    on user_credentials (id);


