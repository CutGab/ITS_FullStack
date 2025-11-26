create domain RealGEZ as real
	check(value is NOT NULL and value >= 0);

create type indirizzo as (
	via varchar(100),
	civico varchar(100)
);

-- ! TABELLE ! --

create table Impiegato (
	codice integer not null,
	nome varchar(100) not null,
	cognome varchar(100) not null,
	nascita date not null,
	stipendio RealGEZ not null,
	primary key(codice)
);

create table Progetto (
	codice varchar(5) not null,
	nome varchar(100) not null,
	budget RealGEZ not null,
	primary key(codice)
);

create table Dipartimento (
	codice integer not null,
	nome varchar(100) not null,
	indirizzo indirizzo,
	codice_Imp integer not null,
	primary key(codice),
	foreign key(codice_Imp)
		references Impiegato(codice)
	-- v.incl codice occorre almeno una volta in Dip_Tel(codice_Dip)
);

create table Telefono (
	telefono varchar(15) not null,
	primary key(telefono)
	-- v.incl telefono occorre almeno una volta in Dip_Tel(id_Telefono)
);

create table Dip_Tel (
	codice_Dip integer not null,
	id_Telefono varchar(15) not null,
	foreign key(codice_Dip)
		references Dipartimento(codice),
	foreign key(id_Telefono)
		references Telefono(telefono)
);

create table coinvolto(
	codice_Imp integer not null,
	codice_Prog integer not null,
	primary key(codice_Imp, codice_Prog),
	foreign key(codice_Imp)
		references Impiegato(codice),
	foreign key(codice_Prog)
		references Dipartimento(codice)
);

create table afferenza (
	codice_Imp integer not null,
	codice_Dip integer not null,
	data_afferenza date not null,
	primary key(codice_Imp),
	foreign key(codice_Imp)
		references Impiegato(codice),
	foreign key(codice_Dip)
		references Dipartimento(codice)
);
