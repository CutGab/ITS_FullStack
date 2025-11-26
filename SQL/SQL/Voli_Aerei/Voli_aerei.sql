CREATE DOMAIN str as varchar(200);

CREATE DOMAIN IntGEZ as integer
        check (value >= 0);
        
CREATE DOMAIN IntGZ as integer
        check (value > 0);

CREATE DOMAIN IntGE1900 as integer
        check (value >= 1900);

CREATE DOMAIN codice_volo as varchar(6);

CREATE DOMAIN codice_IATA as varchar(3);



CREATE TABLE nazione(
	nome str,
	primary key(nome)
);


CREATE TABLE città(
	nome_città str not null,
	n_abitanti IntGEZ not null,

	-- accorpo  nazione 
	nome_nazione str not null,
	foreign key (nome_nazione)
		references nazione(nome),

	primary key(nome_nazione, nome_città)
);


CREATE TABLE aereoporto(
	id serial,
	codice_IATA codice_IATA not null,
	nome str not null,

	-- accorop aer_città
	nome_città str not null,
	nome_nazione str not null,
	primary key(id),
	foreign key (nome_nazione, nome_città)
		references città(nome_nazione, nome_città)
);


CREATE TABLE compagnia(
	id serial,
	nome str not null,
	fondazione IntGE1900 not null,

	-- accorop comp_cit
	nome_città str not null,
	nome_nazione str not null,
	primary key(id),
	foreign key (nome_nazione, nome_città)
		references città(nome_nazione, nome_città)
);


CREATE TABLE volo(
	id serial,
	id_volo	 codice_volo not null,
	durata_minuti IntGZ,

	-- accorpo arrivo
	arrivo integer not null,
	primary key(id),
	foreign key (arrivo)
		references aereoporto(id),

	-- accorpo partenza
	partenza integer not null,
	foreign key (partenza)
		references aereoporto(id),

	-- accorpo volo_comp
	codice_compagnia integer,
	foreign key (codice_compagnia)
		references compagnia(id)
);