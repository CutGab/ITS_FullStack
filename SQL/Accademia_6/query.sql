-- 1. Quanti sono gli strutturati di ogni fascia?

SELECT p.posizione, count(*)
FROM Persona p
GROUP BY posizione;

-- 2. Quanti sono gli strutturati con stipendio >= 40000?

SELECT count(*)
FROM Persona p
WHERE p.stipendio >= 40000;

-- 3. Quanti sono i progetti già finiti che superano il budget di 50000?

SELECT count(*)
FROM Progetto p
WHERE p.fine is not NULL
AND p.budget >= 50000;

--4. Qual è la media, il massimo e il minimo delle ore delle attività relative al progetto 'Pegasus'?

SELECT round(avg(oreDurata), 2) as durata_media, max(oreDurata), min(oreDurata)
FROM AttivitaProgetto ap, Progetto pr
WHERE ap.progetto = pr.id
AND ap.progetto = 1;

--5. Quali sono le medie, i massimi e i minimi delle ore giornaliere dedicate al progetto 'Pegasus' da ogni singolo docente?

SELECT p.nome, p.cognome, round(avg(oreDurata), 2) as durata_media, max(oreDurata), min(oreDurata)
FROM AttivitaProgetto ap, Persona p, Progetto pr
WHERE ap.persona = p.id
AND pr.id = ap.progetto
AND ap.progetto = 1
GROUP BY(p.id)

--6. Qual è il numero totale di ore dedicate alla didattica di ogni docente?

SELECT p.nome, p.cognome, sum(oreDurata) as tot_ore
FROM AttivitaNonProgettuale anp, Persona p
WHERE anp.persona = p.id
AND anp.tipo = 'Didattica'
GROUP BY (p.id);


--7. Qual è la media, il massimo e il minimo degli stipendi dei ricercatori?

SELECT avg(stipendio), max(stipendio) as max_stipendio, min(stipendio) as min_stipendio
FROM Persona p
WHERE p.posizione = 'Ricercatore';

--8. Quali sono le medie, i massimi e i minimi degli stipendi dei ricercatori, dei professori associati e dei professori ordinari?

SELECT p.posizione, avg(stipendio), max(stipendio) as max_stipendio, min(stipendio) as min_stipendio
FROM Persona p
GROUP BY (p.posizione);

--9. Quante ore "Ginevra Riva" ha dedicato al progetto nel quale ha lavorato?                                                                                                                               

SELECT p.nome, p.cognome, ap.progetto, sum(ap.oredurata) as ore_totali_Ginevra
FROM Persona p, AttivitaProgetto ap
WHERE p.id = ap.persona
AND p.nome = 'Ginevra'
AND p.cognome = 'Riva'
GROUP BY (p.id, ap.progetto);

--10. Qual è il nome dei progetti su cui lavorano più di due strutturati?

SELECT pr.nome
FROM AttivitaProgetto ap, Progetto pr
WHERE ap.progetto = pr.id
GROUP BY(ap.progetto, pr.nome)
HAVING count(ap.persona) >= 2;

--11. Quali sono i professori associato che hanno lavorato su più di un progetto?

SELECT p.id, p.nome, p.cognome, COUNT(ap.id) AS num_progetti
FROM AttivitaProgetto ap, Persona p
WHERE ap.persona = p.id
AND p.posizione = 'Professore Associato'
GROUP BY(p.id)
HAVING COUNT(ap.progetto) > 1;