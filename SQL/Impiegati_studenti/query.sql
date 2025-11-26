-- 1. Quali sono i nomi degli impiegati nati a partire dall'anno 1965?

SELECT nome FROM persona p, impiegato i WHERE p.cf = i.persona AND EXTRACT(YEAR FROM nascita) >= 1965;

-- 2. Quali sono i nomi di tutti i progetti?

SELECT nome FROM progetto;

-- 3. Quali sono gli stipendi dei direttori?

SELECT stipendio FROM impiegato WHERE ruolo = 'Direttore';

-- 4. Quanti sono i progettisti?

SELECT count(ruolo) FROM impiegato p WHERE p.ruolo = 'Progettista';

-- 5. Quanti sono i responsabili?

SELECT count(impiegato) FROM responsabile;

-- 6. Quanti sono i progettisti che non sono responsabili? 

SELECT count(impiegato) FROM responsabile r, impiegato i WHERE i.ruolo = 'Progettista' AND i.persona != r.impiegato; -- SBAGLIATA --

-- 6. Quanti sono i progettisti che non sono responsabili? 

SELECT count(*) FROM impiegato i WHERE i.ruolo = 'Progettista' AND i.persona NOT IN (SELECT impiegato FROM responsabile); -- CORRETTA --

-- 7. Qual è lo stipendio medio dei segretari?

SELECT avg(stipendio) as media from impiegato i where i.ruolo = 'Segretario';

-- 8. Qual è l'età della/o studente meno giovane?

SELECT max(EXTRACT(YEAR from current_date) - EXTRACT(YEAR from nascita)) from persona, studente where studente.persona = persona.cf;

-- 9. Quanti sono i direttori che hanno assolto agli obblighi militari?

SELECT count(impiegato) from impiegato, persona WHERE impiegato.ruolo = 'Direttore' and persona.pos_mil = 'Assolto' and persona.cf = impiegato.persona;

-- 9a. Quanti sono gli impiegati che hanno una posizione militare diversa da "Assolto"?

SELECT count(*) FROM impiegato, persona WHERE persona.cf = impiegato.persona AND persona.pos_mil != 'Assolto';

-- 10. Quanti sono i progetti di cui è responsabile un'impiegata con almeno due figli?

SELECT count(progetto) FROM resp_prog, persona WHERE resp_prog.responsabile = persona.cf AND persona.maternita >= 2;