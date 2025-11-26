-- 1. Quali sono le persone con stipendio di al massimo 40000 euro [2 punti]
SELECT p.id, p.nome, p.cognome, p.stipendio 
FROM Persona p
WHERE p.stipendio <= 40000;

-- 2. Quali sono i ricercatori che lavorano ad almeno un progetto e hanno uno stipendio di al massimo 40000 [2 punti]

SELECT p.id, p.nome, p.cognome, p.stipendio, p.posizione
FROM persona p, attivitaprogetto ap 
WHERE p.id = ap.persona
AND p.posizione = 'Ricercatore'
AND p.stipendio <= 45000;

-- 3. Qual è il budget totale dei progetti nel db [2 punti]

SELECT sum(budget) as budget_totale
FROM progetto;

-- 4. Qual è il budget totale dei progetti a cui lavora ogni persona. Per ogni persona restituire nome, cognome e
-- budget totale dei progetti nei quali è coinvolto. [3 punti]

SELECT per.id, per.nome, per.cognome, sum(p.budget)
FROM persona per, progetto p, attivitaprogetto ap
WHERE per.id = ap.persona
AND ap.progetto = p.id
GROUP BY per.id;

-- 5. Qual è il numero di progetti a cui partecipa ogni professore ordinario. Per ogni professore ordinario,
-- restituire nome, cognome, numero di progetti nei quali è coinvolto [3 punti]

SELECT p.id, p.nome, p.cognome, count(ap.progetto) as progetti_in_corso
FROM persona p, attivitaprogetto ap
WHERE p.id = ap.persona
AND p.posizione = 'Professore Ordinario'
GROUP BY p.id;

-- 6. Qual è il numero di assenze per malattia di ogni professore associato. Per ogni professore associato,
-- restituire nume, cognome e numero di assenze per malattia [3 punti]

SELECT p.id, p.nome, p.cognome, count(a.giorno) AS numero_assenze FROM assenza a, persona p
WHERE p.posizione = 'Professore Associato'
AND p.id = a.persona
GROUP BY p.id;

-- 7. Qual è il numero totale di ore, per ogni persona, dedicate al progetto con id ‘5’. Per ogni persona che lavora al
-- progetto, restituire nome, cognome e numero di ore totali dedicate ad attività progettuali relative al progetto 
-- [4 punti]

SELECT p.id, p.nome, p.cognome, sum(ap.oredurata) as ore_totali
FROM persona p, attivitaprogetto ap
WHERE p.id = ap.persona
AND ap.progetto = 1
GROUP BY p.id;

-- 8. Qual è il numero medio di ore delle attività progettuali svolte da ogni persona. Per ogni persona, restituire nome,
-- cognome e numero medio di ore delle sue attività progettuali (in qualsivoglia progetto) [3 punti]

SELECT p.id, p.nome, p.cognome, avg(ap.oredurata) as ore_medie
FROM persona p, attivitaprogetto ap
WHERE p.id = ap.persona
GROUP BY p.id;

-- 9. Qual è il numero totale di ore, per ogni persona, dedicate alla didattica. Per ogni persona che ha svolto attività
-- didattica, restituire nome, cognome e numero di ore totali dedicate alla didattica [4 punti]

SELECT p.id, p.nome, p.cognome, sum(anp.oredurata) as ore_totali_didattica
FROM persona p, attivitanonprogettuale anp
WHERE p.id = anp.persona
AND anp.tipo = 'Didattica'
GROUP BY p.id;

-- 10. Quali sono le persone che hanno svolto attività nel WP di id ‘0’ del progetto con id ‘1’. Per ogni persona, restituire
-- il numero totale di ore svolte in attività progettuali per il WP in questione [4 punti]

SELECT p.id, p.nome, p.cognome, sum(ap.oredurata) as ore_totali
FROM persona p, attivitaprogetto ap
WHERE p.id = ap.persona
AND ap.wp = 0
AND ap.progetto = 1
GROUP BY p.id;
