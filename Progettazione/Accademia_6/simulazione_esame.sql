-- Active: 1758181565827@@LocalHost@5432@accademia
-- 1. Elencare tutti i progetti la cui fine è successiva al 2023-12-31. [2 punti]

SELECT  * 
FROM Progetto 
WHERE fine > '2023-12-31';

-- 2. Contare il numero totale di persone per ciascuna posizione (Ricercatore, Professore Associato, Professore Ordinario). [3 punti]

SELECT posizione, count(*) 
FROM Persona 
GROUP BY posizione;

-- 3. Restituire gli id e i nomi delle persone che hanno almeno un giorno di assenza per "Malattia". [2 punti]

SELECT DISTINCT p.id, nome FROM persona p, assenza a
WHERE p.id = a.persona
AND a.tipo = 'Malattia';

-- 4. Per ogni tipo di assenza, restituire il numero complessivo di occorrenze. [3 punti]

SELECT tipo, count(*) from assenza
GROUP BY tipo;

-- 5. Calcolare lo stipendio massimo tra tutti i "Professori Ordinari". [2 punti]

SELECT max(stipendio) from persona
WHERE posizione = 'Professore Ordinario';

-- 6. Quali sono le attività e le ore spese dalla persona con id 1O nelle attività del progetto con id 1, ordinate in ordine 
-- decrescente. Per ogni attività, restituire l’id, il tipo e il numero di ore. [3 punti]

SELECT a.id as persona, a.tipo, a.oredurata 
FROM attivitaprogetto a
WHERE a.persona = 10
AND a.progetto = 1
ORDER BY oredurata desc;

-- 7. Quanti sono i giorni di assenza per tipo e per persona. Per ogni persona e tipo di assenza, restituire nome, cognome,
-- tipo assenza e giorni totali. [4 punti]

SELECT p.id, p.nome, p.cognome, a.tipo, count(a.giorno) as giorni from persona p, assenza a
WHERE p.id = a.persona
GROUP BY p.id, p.nome, p.cognome, a.tipo;


-- (EXTRA) quante sono le coppie di persone distinte con lo stesso nome e lo stesso cognome
select p.id, p1.id, p.nome, p.cognome
from persona p, persona p1
where p.id <> p1.id 
    and p.nome = p1.nome and p.cognome = p1.cognome
    and p.id > p1.id;

-- 8. Restituire tutti i “Professori Ordinari” che hanno lo stipendio massimo. Per ognuno, restituire id, nome e cognome [4 punti]

SELECT p.id, p.nome, p.cognome
FROM persona p
WHERE p.posizione = 'Professore Ordinario'
AND p.stipendio = (
        SELECT MAX(p.stipendio)
        FROM persona p
        WHERE p.posizione = 'Professore Ordinario');

-- 9. Restituire la somma totale delle ore relative alle attività progettuali svolte dalla persona con id = 3 e con durata
-- minore o uguale a 3 ore. [3 punti]

SELECT sum(oredurata) AS totale_ore FROM attivitaprogetto a
WHERE a.persona = 0
AND oredurata < 10;

-- 10. Restituire gli id e i nomi delle persone che non hanno mai avuto assenze di tipo "Chiusura Universitaria" [4 punti]

SELECT p.id, p.nome from persona p, assenza a
WHERE p.id = a.persona
AND  a.tipo != 'Chiusura Universitaria'
GROUP BY p.id;
