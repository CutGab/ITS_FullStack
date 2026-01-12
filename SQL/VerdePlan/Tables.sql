-- Active: 1767946474283@@Localhost@5432@cittaverde

create table specie (
    n_scientifico stringa primary key,
    n_comune stringa
);
create table areaverde(
    id serial primary key,
    lat latitudine not null,
    lon longitudine not null,
    is_fruibile bool not null,
    is_sensibile bool not null,

    check (is_sensibile=false or is_fruibile=true) --"Se A allora B" --> NOT A OR B

);

create table soggettoverde (
    id serial primary key,
    data date not null,
    specie stringa not null, --accorpa l'assoc. tra sogg. verde e specie --
    Foreign Key (specie) 
        REFERENCES specie(n_scientifico),
    area integer not null, -- Accorpa l'assoc tra sogg. verde e areaverde
    Foreign Key (area) 
        REFERENCES areaverde(id)
);

create table intervento (
    id serial primary key,
    inizio TIMESTAMP not null,
    durata intgz not null,
    priorita priorita not null,
    area integer not null, -- Accorpa l'assoc tra intervento e areaverde --
    Foreign Key (area) 
        REFERENCES areaverde (id)
);

create table interventoassegnato (
    id_intervento integer primary key, -- Accorpa ia_isa_i (per legge!) --
    Foreign Key (id_intervento) 
        REFERENCES intervento (id),
    fine TIMESTAMP -- (id_intervento) occorre in assegna(interventoassegnato)
);

create table operatore (
    cf cf primary key,
    nome stringa not null,
    cognome stringa not null,
    inizio date not null,
    fine date -- Se ci fosse il vincolo, avrebbe anche check(value is null or value > inizio) --
);

create table assegna (

    interventoassegnato integer not null,
    operatore cf not null,
    istante timestamp not null,

    Foreign Key (interventoassegnato) 
        REFERENCES interventoassegnato(id_intervento),

    Foreign Key (operatore) 
        REFERENCES operatore (cf),

    primary key(interventoassegnato,operatore)
)

