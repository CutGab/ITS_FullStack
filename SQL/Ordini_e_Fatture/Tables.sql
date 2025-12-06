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
	indirizzo indirizzo not null,
	primary key(nome)
);

CREATE TABLE Fornitore(
	ragione_sociale varchar(100) not null,
	partita_iva partita_iva
)
