-- QUERY 1 --
SELECT DISTINCT cognome 
FROM persona;


-- QUERY 2 --
SELECT nome, cognome 
FROM persona
WHERE posizione = 'Ricercatore';


-- QUERY 3 --
SELECT cognome 
FROM persona 
WHERE posizione = 'Professore Associato' 
AND cognome LIKE 'V%';


-- QUERY 4 --
SELECT cognome 
FROM persona 
WHERE (posizione = 'Professore Associato' 
OR posizione = 'Professore Ordinario') 
AND cognome LIKE 'V%';


-- QUERY 5 --
SELECT nome 
FROM progetto
WHERE fine < current_date;


-- QUERY 6 --
SELECT nome
FROM progetto 
ORDER BY inizio;


-- QUERY 7 --
SELECT nome 
FROM wp 
ORDER BY nome ASC;


-- QUERY 8 --
SELECT DISTINCT tipo 
FROM assenza;


-- QUERY 9 --
SELECT DISTINCT tipo 
FROM attivitaprogetto;


-- QUERY 10 --
SELECT DISTINCT giorno
FROM attivitanonprogettuale
WHERE tipo = 'Didattica' 
ORDER BY giorno ASC;