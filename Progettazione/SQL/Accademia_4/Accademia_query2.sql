-- QUERY 1 --

SELECT wp.id, wp.nome, wp.inizio, wp.fine 
FROM wp, progetto p 
WHERE p.nome = 'Pegasus' 
AND wp.progetto = p.id;

-- QUERY 2 --

SELECT distinct p.id, p.nome, p.cognome, p.posizione 
FROM persona p, progetto pr, attivitaprogetto ap
WHERE pr.id = ap.progetto 
AND ap.persona = p.id
AND pr.nome = 'Pegasus'
ORDER BY cognome DESC;

-- QUERY 3 --

SELECT distinct p.id, p.nome, p.cognome, p.posizione 
FROM persona p, progetto pr, attivitaprogetto ap
WHERE pr.id = ap.progetto 
AND ap.persona = p.id
AND pr.nome = 'Pegasus'
GROUP BY p.id, p.nome, p.cogno me, p.posizione
HAVING(count(ap.persona) > 1);

-- QUERY 4 --

SELECT distinct p.id, p.nome, p.cognome 
FROM assenza a, persona p 
WHERE p.id = a.persona 
AND p.posizione = 'Professore Ordinario' 
AND a.tipo = 'Malattia';

-- QUERY 5 --

SELECT p.id, p.nome, p.cognome 
FROM assenza a, persona p 
WHERE p.id = a.persona 
AND p.posizione = 'Professore Ordinario' 
AND a.tipo = 'Malattia' 
GROUP BY (p.id, p.nome, p.cognome) 
HAVING(count(a.persona) > 1);

-- QUERY 6 --

SELECT distinct p.id, p.nome, p.cognome 
FROM persona p, attivitanonprogettuale anp 
WHERE anp.persona = p.id 
AND anp.tipo = 'Didattica' 
AND p.posizione = 'Ricercatore' 
ORDER BY p.id DESC;

-- QUERY 7 --

SELECT p.id, p.nome, p.cognome 
FROM persona p, attivitanonprogettuale anp 
WHERE anp.persona = p.id 
AND anp.tipo = 'Didattica' 
AND p.posizione = 'Ricercatore' 
GROUP BY(p.id, p.nome, p.cognome) 
HAVING count(anp.persona) > 1;

-- QUERY 8 --

SELECT distinct p.id, p.nome, p.cognome 
FROM persona p, attivitaprogetto ap, attivitanonprogettuale anp 
WHERE ap.persona = p.id 
AND anp.persona = p.id 
AND ap.giorno = anp.giorno;

-- QUERY 9 --

SELECT p.id, p.nome, p.cognome, ap.giorno, pr.nome as prj, ap.oredurata as h_prj, anp.tipo as att_noprj, anp.oredurata as h_noprj 
FROM persona p, attivitaprogetto ap, attivitanonprogettuale anp, progetto pr
WHERE ap.persona = p.id 
AND anp.persona = p.id 
AND ap.giorno = anp.giorno
AND pr.id = ap.progetto;

-- QUERY 10 --

SELECT distinct p.id, p.nome, p.cognome 
FROM persona p, assenza a, attivitaprogetto ap
WHERE p.id = a.persona
AND a.giorno = ap.giorno
AND p.id = ap.persona;

-- QUERY 11 --

SELECT distinct p.id, p.nome, p.cognome, ap.giorno, a.tipo as causa_ass, pr.nome as progetto, ap.oreDurata as ore_att_prj
FROM persona p, assenza a, attivitaprogetto ap, progetto pr
WHERE p.id = a.persona
AND a.giorno = ap.giorno
AND p.id = ap.persona
AND pr.id = ap.progetto;

-- QUERY 12 --

SELECT wp.nome 
FROM wp, progetto p
WHERE p.id = wp.progetto
GROUP BY (wp.nome) 
HAVING count(distinct wp.progetto) > 1;
