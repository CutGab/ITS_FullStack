-- Active: 1758181565827@@LocalHost@5432@accademia
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