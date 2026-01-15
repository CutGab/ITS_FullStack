CREATE TABLE Falesia (
    nome varchar NOT NULL,
    latitudine Lat NOT NULL,
    longitudine Long NOT NULL,
    PRIMARY KEY(nome)

     -- v.incl(nome) occorre in Settore(falesia) --
);


CREATE TABLE Settore (
    nome varchar NOT NULL,
    esposizione Coordinate NOT NULL,
    falesia varchar NOT NULL,
    PRIMARY KEY(falesia, nome),

    Foreign Key (falesia) 
        REFERENCES Falesia(nome)
);

CREATE TABLE Grado (
    id SERIAL NOT NULL,
    nome varchar NOT NULL,
    valore varchar NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE Persona (
    username varchar NOT NULL,
    PRIMARY KEY(username)
);

CREATE TABLE Arrampicatore (
    nome varchar,
    cognome varchar,
    persona varchar NOT NULL,
    PRIMARY KEY(persona),

    Foreign Key (persona) 
        REFERENCES Persona(username)
);

CREATE TABLE Chiodatore (
    persona varchar NOT NULL,
    PRIMARY KEY(persona),

    Foreign Key (persona) 
        REFERENCES Persona(username)
);

CREATE TABLE Via (
    nome varchar NOT NULL,
    lunghezza IntGEZ NOT NULL,
    n_spit IntGZ NOT NULL,
    settore varchar NOT NULL,
    falesia varchar NOT NULL,
    grado integer NOT NULL,
    chiodatore varchar NOT NULL,
    PRIMARY KEY (settore, nome),
    UNIQUE(grado, chiodatore),

    Foreign Key (grado) 
        REFERENCES Grado(id),

    Foreign Key (settore, falesia) 
        REFERENCES Settore(falesia, nome),

    Foreign Key (chiodatore) 
        REFERENCES Chiodatore (persona)
);

CREATE TABLE Salita (
    id serial NOT NULL,
    data DATE NOT NULL,
    via varchar,
    nome varchar,
    arrampicatore varchar,
    PRIMARY KEY(id),
    UNIQUE(arrampicatore, via),

    Foreign Key (via, nome) 
        REFERENCES Via (settore, nome),

    Foreign Key (arrampicatore) 
        REFERENCES Arrampicatore (persona)
);

CREATE TABLE Flash (
    salita serial NOT NULL,

    PRIMARY KEY(salita),

    Foreign Key (salita) 
        REFERENCES Salita(id)
);

CREATE TABLE AVista (
    salita serial NOT NULL,
    PRIMARY KEY(salita),

    Foreign Key (salita) 
        REFERENCES Salita(id)
);

CREATE TABLE Ripetuta (
    salita serial NOT NULL,

    PRIMARY KEY(salita),

    Foreign Key (salita) 
        REFERENCES Salita(id)

    -- v.incl(salita) occorre in Tentativo(ripetuta) --

);

CREATE TABLE Tentativo (
    id serial NOT NULL,
    note varchar,
    ripetuta integer,
    PRIMARY KEY(id),

    Foreign Key (ripetuta) 
        REFERENCES Ripetuta(salita)
);