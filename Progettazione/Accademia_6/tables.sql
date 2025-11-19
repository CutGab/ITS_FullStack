CREATE table Persona (

	id PosInteger primary key,
	nome StringaM not null,
	cognome StringaM not null,
	posizione Strutturato not null,
	stipendio Denaro not null

);


CREATE table Progetto (

	id PosInteger primary key,
	nome StringaM not null unique,
	inizio date not null,
	fine date not null,
	budget Denaro not null,

	check (inizio < fine)

);


CREATE table WP (

	progetto PosInteger not null,
	id PosInteger not null,
	nome StringaM not null,
	inizio date not null,
	fine date not null,

	check (inizio < fine),

	foreign key (progetto)
		references Progetto(id),

	unique (progetto, nome),

	primary key (progetto, id)

);


CREATE table AttivitaProgetto (

	id PosInteger primary key,
	persona PosInteger not null,
	progetto PosInteger not null,
	wp PosInteger not null,
	giorno date not null,
	tipo LavoroProgetto not null,
	oreDurata NumeroOre not null,

	foreign key (persona)
		references Persona(id),
	foreign key (progetto, wp)
		references 	WP(progetto, id)
);


CREATE table AttivitaNonProgettuale (

	id PosInteger primary key,
	persona PosInteger not null,
	tipo LavoroNonProgettuale not null,
	giorno date not null,
	oreDurata NumeroOre not null,

	foreign key (persona)
		references Persona(id)

);


CREATE table Assenza (

	id PosInteger primary key,
	persona PosInteger not null,
	tipo CausaAssenza not null,
	giorno date not null,

	unique (persona, giorno),

	foreign key (persona)
		references Persona(id)

);