--1. Quante sono le compagnie che operano (sia in arrivo che in partenza) nei diversi aeroporti?

SELECT a.codice, nome, count(DISTINCT ap.comp) as num_compagnie
FROM Aeroporto a, ArrPart ap
WHERE ap.partenza = a.codice
OR ap.arrivo = a.codice
GROUP BY(a.nome, a.codice);

--2. Quanti sono i voli che partono dall'aeroporto "HTR" e hanno una durata di almeno 100 minuti=

SELECT count(*) as num_voli
FROM Volo v, ArrPart ap
WHERE v.codice = ap.codice
AND v.comp = ap.comp
AND ap.partenza = 'HTR'
AND v.durataMinuti >= 100;

--3. Quanti sono gli aeroporti sui quali opera la compagnia "Apitalia", per ogni nazione nella quale opera?

SELECT nazione, count(DISTINCT la.aeroporto)
FROM LuogoAeroporto la, ArrPart ap
WHERE (ap.partenza = la.aeroporto
OR ap.arrivo = la.aeroporto)
AND ap.comp = 'Apitalia'
GROUP BY (nazione);

--4. Qual è la media, il massimo e il minimo della durata dei voli effettuati dalla compagnia 'MagicFly'?

SELECT avg(durataMinuti) as media, max(durataMinuti) as massimo, min(durataMinuti) as minimo
FROM Volo
WHERE comp = 'MagicFly';

--5. Qual è l'anno di fondazione della compagnia più vecchia che opera in ognuno degli aeroporti?

SELECT a.codice, a.nome, min(c.annofondaz) as anno
FROM Compagnia c, ArrPart ap, Aeroporto a
WHERE c.nome = ap.comp
AND (a.codice = ap.partenza
OR a.codice = ap.arrivo)
GROUP BY (a.codice, a.nome);

--6. Quante sono le nazioni (diverse) raggiungibili da ogni nazione tramite uno o più voli?

SELECT la.nazione, count(DISTINCT la2.nazione) as raggiungibili
FROM LuogoAeroporto la, ArrPart ap, LuogoAeroporto la2
WHERE la.aeroporto = ap.partenza
AND la2.aeroporto = ap.arrivo
AND la2.nazione <> la.nazione
GROUP BY(la.nazione);

--7. Qual è la durata media dei voli che partono da ognuno degli aeroporti?

SELECT a.codice, a.nome, avg(durataMinuti) as media_durata
FROM Volo v, Aeroporto a, ArrPart ap
WHERE a.codice = ap.partenza
AND v.codice = ap.codice
GROUP BY(a.codice, a.nome);

--8. Qual è la durata complessiva dei voli operati da ognuna delle compagnie fondate a partire dal 1950?

SELECT v.comp, sum(durataMinuti) as durata_tot
FROM Volo v, Compagnia c
WHERE v.comp = c.nome
AND c.annofondaz >= '1950'
GROUP BY(v.comp);

--9. Quali sono gli aeroporto nei quali operano esattamente due compagnie?

SELECT a.codice, a.nome
FROM Aeroporto a, Arrpart ap
WHERE (ap.partenza = a.codice
OR ap.arrivo = a.codice)
GROUP BY (a.codice)
HAVING count(DISTINCT ap.comp) = 2;

--10. Quali sono le città con almeno due aeroporti?

SELECT citta
FROM LuogoAeroporto
GROUP BY (citta)
HAVING count(Aeroporto) >= 2;

--11. Qual è il nome delle compagnie i cui voli hanno una durata media maggiore di 6 ore?

SELECT comp
FROM Volo
GROUP BY (comp)
HAVING avg(durataMinuti) > 360;

--12. Qual è il nome delle compagnie i cui voli hanno tutti una durata maggiore di 100 minuti?

SELECT comp
FROM Volo
GROUP BY (comp)
HAVING min(durataMinuti) > 100;