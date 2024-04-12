Gorescu Diana, 
332CC

# Tema 1 ASC- Le Stats Sportif

Organizare
-
1. În *data_ingestor.py* am citit setul de date în format *csv*. Am creat o lista de dicționare (1 dicționar reprezintă 1 rând citit). Uitându-mă în trecut, mi se pare o abordare naivă, întrucât aș fi putut accesa datele mai eficient.
2. În ThreadPool îmi transfer datele citite și cele 2 liste de întrebări pentru taskul *best5* și *worst5*; setez numărul de threaduri; initializez o coadă Queue pentru sincronizarea joburilor, iar la final creez și lansez threadurile din lista. În plus, nefolosind ThreadPoolExecutor, a trebuit să mi definesc eu o funcție de shutdown în care dau join la threaduri.\
În metoda *run()* din clasa TaskRunner apelez funcția numită după numele jobului. Rezultatul acesteia este scris în format json într-un fișier din folderul *results*. Așadar, jobul fiind terminat, îl adaug într-o lista specifică și actualizez și statusul acestuia. În aceeași clasa am implementat pe rând funcții pentru cererile enuntate.
3. Cu ajutorul videoului [1] am înțeles mai bine cum funcționează un request GET/POST. Totodată, cu extensia *Postman*, am reușit să fac debugging mai ușor, vazand pe loc rezultatul al unei cereri. La fiecare cerere de tip POST, îmi cream o structura pentru job pe care îl adăugăm în coadă, creșteam counter-ul de joburi și returnam id-ul jobului proaspăt generat. Un exemplu de structura:
```python
job_struct = {
        "job_id" : job_id ,
        "nume_job" :  "state_mean" , 
        "question_data" : data['question'],
        "nume_stat" : data['state'],
        "status" : "running"
    }
```
4.  Cu ajutorul documentației, am creat și unitteste pentru testarea funcționalității rutelor. Am dat exemple diverse pentru a evidenția corectitudinea lor.
5.  Folosind modulul de logging, în fișier de log *webserver.log*, am afișat toate intrările și ieșirile din rutele implementate. Am folosit nivelul info() și *RotatingFileHandler* pentru a seta numărul maxim de copii istorice și dimensiunea lor.



* Consider că tema este utilă. Am înțeles mai bine ce se întâmplă în spatele unei relații server-client. Am aprofundat atât limbajul Python, cât și gestionarea threadurilor. Fiind o tema destul de migăloasă, am învățat să fac debugging mai ușor, cu ajutorul fișierului de log.
* Cred că implementarea este echilibrată, întrucât are o logică destul de ușor de urmărit.


Implementare
-

* Am implementat mecanică serverului și toate requesturile enunțate. Totodată am făcut partea de Unittesting pentru toate rutele, Logging și încărcarea pe Gît.



Resurse utilizate
-

* https://ocw.cs.pub.ro/courses/asc/laboratoare/02
* [Create A Python API in 12 Minutes](https://www.youtube.com/watch?v=zsYIw6RXjfM) [1]
* https://www.geeksforgeeks.org/python-get-first-n-keyvalue-pairs-in-given-dictionary/
* [Python Logging - Tutorial](https://www.youtube.com/watch?v=urrfJgHwIJA)

Git
-
1. https://github.com/dianagorescu/tema1-ASC.git

