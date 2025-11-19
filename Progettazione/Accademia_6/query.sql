-- 1. Quanti sono gli strutturati di ogni fascia?

SELECT posizione, count(*) as numero
FROM persona
GROUP BY(posizione);

-- 2. Quanti sono gli strutturati con stipendio >= 40000?

SELECT count(*) as numero
FROM persona
WHERE stipendio >= 40000;

-- 3. Quanti sono i progetti già finiti che superano il budget di 50000?

SELECT count(*) as numero
FROM progetto
WHERE budget > 50000
AND fine <= CURRENT_DATE;

--4. Qual è la media, il massimo e il minimo delle ore delle attività relative al progetto 'Pegasus'?

Select avg(oredurata) as media, max(oredurata) as massimo, min(oredurata) as minimo
FROM progetto p, attivitaprogetto ap
WHERE ap.progetto = p.id
AND p.nome = 'Pegasus';

--5. Quali sono le medie, i massimi e i minimi delle ore giornaliere dedicate al progetto 'Pegasus' da ogni singolo docente?

SELECT per.id, per.nome, cognome, avg(oredurata) as media, max(oredurata) as massimo, min(oredurata) as minimo
FROM progetto p, attivitaprogetto ap, persona per
WHERE ap.progetto = p.id
AND per.id = ap.persona
AND p.nome = 'Pegasus'
GROUP BY(per.id);

--6. Qual è il numero totale di ore dedicate alla didattica di ogni docente?

SELECT p.id, nome, cognome, sum(oreDurata) as ore_didattica from persona p, AttivitaNonProgettuale anp
WHERE p.id = anp.persona
AND anp.tipo = 'Didattica'
GROUP BY(p.id);

--7. Qual è la media, il massimo e il minimo degli stipendi dei ricercatori?

SELECT avg(stipendio) as media, max(stipendio) as massimo, min(stipendio)
FROM persona
WHERE posizione = 'Ricercatore';

--8. Quali sono le medie, i massimi e i minimi degli stipendi dei ricercatori, dei professori associati e dei professori ordinari?

SELECT posizione, avg(stipendio) as media, max(stipendio) as massimo, min(stipendio) as minimo
FROM persona per
WHERE (per.posizione = 'Professore Associato' OR per.posizione = 'Professore Ordinario' OR per.posizione = 'Ricercatore')
GROUP BY(per.posizione);

--9. Quante ore "Ginevra Riva" ha dedicato al progetto nel quale ha lavorato?

select pr.id as id_progetto, pr.nome as progetto, sum(oreDurata) as totale_ore
FROM persona p, attivitaprogetto ap, progetto pr
WHERE p.id = ap.persona
AND pr.id = ap.progetto
AND p.nome = 'Ginevra'
AND p.cognome = 'Riva'
GROUP BY(pr.id, pr.id);                                                                                                                                  


--10. Qual è il nome dei progetti su cui lavorano più di due strutturati?

SELECT pro.id, pro.nome as progetto
FROM Progetto pro, AttivitaProgetto ap  
WHERE pro.id = ap.progetto
GROUP BY(pro.nome, pro.id)
HAVING count(DISTINCT ap.persona) >= 2;

--11. Quali sono i professori associato che hanno lavorato su più di un progetto?

SELECT p.id, p.nome, p.cognome
FROM persona p, attivitaprogetto ap
WHERE p.id = ap.persona
AND p.posizione = 'Professore Associato'
GROUP BY (p.id, p.nome, p.cognome)
HAVING count(DISTINCT ap.progetto) > 1;