-- Active: 1767946474283@@Localhost@5432@cittaverde

create domain stringa as varchar;

create domain intgz as integer
    check(value > 0);

CREATE DOMAIN latitudine as REAL
    CHECK (VALUE BETWEEN -90 AND 90);

CREATE DOMAIN longitudine as REAL
    CHECK (VALUE BETWEEN -180 AND 180);

CREATE DOMAIN priorita as INTEGER
    CHECK (VALUE BETWEEN 1 AND 10);

CREATE DOMAIN CF as CHAR(16);
