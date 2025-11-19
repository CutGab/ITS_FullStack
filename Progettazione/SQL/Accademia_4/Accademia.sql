CREATE type Strutturato AS enum (	
	'Ricercatore', 
	'Professore Associato', 
	'Professore Ordinario'
);


CREATE type LavoroProgetto AS enum (	
	'Ricerca e Sviluppo', 
	'Dimostrazione', 
	'Management', 
	'Altro'
);


CREATE type LavoroNonProgettuale AS enum (	
	'Didattica', 
	'Ricerca', 
	'Missione', 
	'Incontro Dipartimentale', 
	'Incontro Accademico', 
	'Altro'
);


CREATE type CausaAssenza AS enum (	
	'Chiusura Universitaria', 
	'Maternita', 
	'Malattia'
);



CREATE DOMAIN PosInteger AS integer
	check (value >= 0);


CREATE DOMAIN StringaM AS varchar (100);


CREATE DOMAIN NumeroOre AS integer
	check (value >= 0 and value <= 8);


CREATE DOMAIN Denaro AS real
	check (value >= 0);

-- TABELLE --

CREATE TABLE Persona (
	id PosInteger,
	nome StringaM not null,
	cognome StringaM not null,
	posizione Strutturato not null,
	stipendio Denaro not null,
	primary key(id)
);


CREATE TABLE Progetto (
	id PosInteger,
	nome StringaM not null unique,
	inizio date not null,
	fine date not null,
	budget Denaro not null,
	primary key (id),

	check (inizio < fine)
);


CREATE TABLE WP (
	progetto PosInteger not null,
	id PosInteger not null,
	nome StringaM not null,
	inizio date not null,
	fine date not null,
	primary key (progetto, id),

	check (inizio < fine),

	foreign key (progetto)
		references Progetto(id),

	unique (progetto, nome)
);


CREATE TABLE AttivitaProgetto (
	id PosInteger,
	persona PosInteger not null,
	progetto PosInteger not null,
	wp PosInteger not null,
	giorno date not null,
	tipo LavoroProgetto not null,
	oreDurata NumeroOre not null,
	primary key(id),

	foreign key (persona)
		references Persona(id),
	foreign key (progetto, wp)
		references 	WP(progetto, id)
);


CREATE TABLE AttivitaNonProgettuale (
	id PosInteger,
	persona PosInteger not null,
	tipo LavoroNonProgettuale not null,
	giorno date not null,
	oreDurata NumeroOre not null,
	primary key(id),

	foreign key (persona)
		references Persona(id)
);


CREATE TABLE Assenza (

	id PosInteger,
	persona PosInteger not null,
	tipo CausaAssenza not null,
	giorno date not null,
	primary key (id),

	unique (persona, giorno),

	foreign key (persona)
		references Persona(id)
);