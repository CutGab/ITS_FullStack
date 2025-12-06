CREATE DOMAIN RealGEZ AS real
check(value is NOT NULL and value >= 0);

CREATE DOMAIN CAP AS char(5) 
CHECK (value ~ '[0-9]{5}'); 

CREATE TYPE Indirizzo AS ( 
        via varchar(100), 
        cap CAP, 
        civico varchar(5) 
);

CREATE TYPE StatoOrdine AS enum (
        'Ricercatore',
        'Professore Associato',
        'Professore Ordinario'
);

CREATE DOMAIN Email AS varchar(100)
CHECK (value ~ '^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Za-z]{2,}\b$');

CREATE DOMAIN PartitaIVA AS varchar(11);

CREATE DOMAIN Telefono AS varchar(15);

CREATE DOMAIN anni_servizio AS integer
CHECK (value >= 0);

CREATE DOMAIN CodiceFiscale AS varchar(16);

CREATE DOMAIN RealGZ AS real
CHECK(value >= 0 and value <= 1);

-- ! TABELLE ! --

CREATE TABLE Nazione (
        nome varchar(100) not null,
        primary key(nome)
);

CREATE TABLE Regione(
        nome varchar(100) not null,
        nazione varchar(100) not null,
        foreign key (nazione)
                references Nazione(nome)
        primary key(nome, nazione)
);

CREATE TABLE Citta(
        nome varchar(100) not null,
        regione varchar(100), not null
        nazione varchar(100) not null,
        foreign key (regione)
                references regione(nome),
        foreign key (nazione)
                references nazione(nome),
        primary key(nome)
);

CREATE TABLE Direttore(
        nome varchar(100) not null,
        cognome varchar(100) not null,
        data_nascita date not null,
        anni_di_servizio anni_servizio not null,
        cf CodiceFiscale not null,
        primary key(CodiceFiscale)
);

CREATE TABLE Dipartimento(
        nome varchar(100) not null,
        indirizzo Indirizzo not null,
        primary key(nome)
);

CREATE TABLE Fornitore(
        id serial,
        ragione_sociale varchar(100) not null,
        partita_iva PartitaIVA not null,
        indirizzo Indirizzo not null,
        telefono Telefono not null,
        email Email not null
        primary key(id)
);

CREATE TABLE Ordine(
        id serial,
        data_stipula date,
        imponibile RealGEZ,
        aliquota_iva RealGZ,
        stato StatoOrdine
        primary key(id)
);
