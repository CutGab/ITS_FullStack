-- Active: 1758181565827@@LocalHost@5432@cielo

create domain PosInteger as integer check (value >= 0);

create domain StringaM as varchar(100);

create domain CodIATA as
  char(3);