-- Active: 1767946474283@@Localhost@5432@rocklog
CREATE TYPE Coordinate AS Enum (
    'N', 
    'S',
    'W',
    'E'
);

CREATE DOMAIN Lat as REAL
CHECK(value BETWEEN -90 AND 90);

CREATE DOMAIN Long as REAL
CHECK(value BETWEEN -180 AND 180);

CREATE DOMAIN IntGEZ as Integer
CHECK(VALUE > 0);

CREATE DOMAIN IntGZ as Integer
CHECK(VALUE >= 0);

