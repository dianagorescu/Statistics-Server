Gorescu Diana, 
332CC

# Tema 1 ASC- Le Stats Sportif

Organizare
-
1. In *data_ingestor.py* am citit setul de date în format *csv*. Am creat o lista de dictionare (1 dictionar reprezinta 1 rand citit). Uitandu-ma in trecut, mi se pare o abordare naiva, intrucat as fi putut accesa datele mai eficient.
2. In ThreadPool imi transfer datele citite si cele 2 liste de intrebari pentru taskul *best5* si *worst5*; initializez numarul de threaduri; initializez o coada Queue pentru sincronizarea joburilor, iar la final creez si lansez threadurile din lista. In plus, nefolosind ThreadPoolExecutor, a trebuit sa mi definesc eu o functia de shutdown in care dau join la threaduri.

***Obligatoriu:*** 


* De făcut referință la abordarea generală menționată în paragraful de mai sus. Aici se pot băga bucăți de cod/funcții - etc.
* Consideri că tema este utilă?
* Consideri implementarea naivă, eficientă, se putea mai bine?

***Opțional:***


* De menționat cazuri speciale, nespecificate în enunț și cum au fost tratate.


Implementare
-

* Am implementat toate functiile din enunt, desi ultimele 2: *state_mean_by_category* si *mean_by_category* necesita optimizare intrucat checkerul imi da timeout cu cea propusa. 



Resurse utilizate
-

* Resurse utilizate - toate resursele publice de pe internet/cărți/code snippets, chiar dacă sunt laboratoare de ASC

Git
-
1. https://github.com/dianagorescu/tema1-ASC.git

Ce să **NU**
-
* Detalii de implementare despre fiecare funcție/fișier în parte
* Fraze lungi care să ocolească subiectul în cauză
* Răspunsuri și idei neargumentate
* Comentarii (din cod) și *TODO*-uri

Acest model de README a fost adaptat după [exemplul de README de la SO](https://github.com/systems-cs-pub-ro/so/blob/master/assignments/README.example.md).