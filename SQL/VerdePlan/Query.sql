-- Query 1 --
select * from areaverde a, soggettoverde s
where s.area = a.id
and s.specie = 'Pinus pinea'
and s.data < CURRENT_DATE - INTERVAL '5 year';

-- Query 2 (SBAGLIATA) --

select count(a) from areaverde a, interventoassegnato ia, intervento i
where a.id = i.area
and i.id = ia.id_intervento
and a.is_sensibile = true
and (i.inizio, ia.fine) OVERLAPS ('2023-10-9', '2023-10-13');

-- Query 2 (GIUSTO) --

SELECT *
FROM areaverde a
WHERE a.is_sensibile = TRUE
  AND a.id NOT IN (
    SELECT i.area
    FROM intervento i, interventoassegnato ia
    WHERE ia.id_intervento = i.id
      AND (i.inizio, ia.fine) OVERLAPS ('2023-10-09', '2023-10-13')
  );

-- Query 3 --

SELECT o.*, COUNT(*) AS num_interventi
FROM operatore o,
     assegna a,
     interventoassegnato ia,
     intervento i
WHERE o.cf = a.operatore
  AND ia.id_intervento = a.interventoassegnato
  AND i.id = ia.id_intervento
  AND i.priorita >= 5
  AND (i.inizio, ia.fine) OVERLAPS ('2023-01-01', '2023-12-31')
GROUP BY o.cf
HAVING COUNT(*) = (
    SELECT MIN(num_interventi)
    FROM (
        SELECT o.cf, COUNT(*) AS num_interventi
        FROM operatore o,
             assegna a,
             interventoassegnato ia,
             intervento i
        WHERE o.cf = a.operatore
          AND ia.id_intervento = a.interventoassegnato
          AND i.id = ia.id_intervento
          AND i.priorita >= 5
          AND (i.inizio, ia.fine) OVERLAPS ('2023-01-01', '2023-12-31')
        GROUP BY o.cf
    )
);

-- Query 4 --

select * 
from areaverde a, soggettoverde sv
where a.id = sv.area
group by(a.id, sv.id)
Having(count(sv.id) >= 10);

-- Query 5 --

select count(a.operatore) 
from intervento i, assegna a
where i.id = a.interventoassegnato
and i.priorita < 4
group by(i.id, a.operatore, a.interventoassegnato);

-- Query 6 --

select i.id, avg(i.durata) as durata_media, avg(ia.fine - i.inizio) as durata_effettiva
from intervento i, interventoassegnato ia
where i.id = ia.id_intervento
and ia.fine is not null
GROUP BY(i.id);

-- Query 7 --

select *
from assegna a, interven
