Gorescu Diana, 
332CC

# Tema 1 ASC- Le Stats Sportif

Organizare
-
1. În *data_ingestor.py* am citit setul de date în format *csv*. Am creat o lista de dicționare (1 dicționar reprezintă 1 rând citit). Uitându-mă în trecut, mi se pare o abordare naivă, întrucât aș fi putut accesa datele mai eficient.
2. În ThreadPool îmi transfer datele citite și cele 2 liste de întrebări pentru taskul *best5* și *worst5*; initializez numărul de threaduri; initializez o coadă Queue pentru sincronizarea joburilor, iar la final creez și lansez threadurile din lista. În plus, nefolosind ThreadPoolExecutor, a trebuit să mi definesc eu o funcția de shutdown în care dau join la threaduri.\
În metodă *run()* din clasa TaskRunner apelez funcția cu numele jobului. Rezultatul acestuia este scris în format json într-un fișier. Așadar, jobul fiind terminat, îl adaug într-o lista specifică și actualizez și statusul acestuia. În aceeași clasa am implementat pe rând funcții pentru cererile de implementat.
3. Cu ajutorul videoului [1] am înțeles mai bine cum funcționează un request GET/POST. Totodată, cu extensia *Postman*, am reușit să fac debugging mai ușor. La fiecare cerere de tip POST, îmi creăm o structura pentru job pe care îl adăugăm în coadă, creșteam counter de joburi și returnăm idul jobului proaspăt generat. Un exemplu de structura:
```python
job_struct = {
        "job_id" : job_id ,
        "nume_job" :  "state_mean" , 
        "question_data" : data['question'],
        "nume_stat" : data['state'],
        "status" : "running"
    }
```
4. Cu ajutorul aplicației *Postman*, am reușit să generez și unittests.


* Consider că tema este utilă. Am înțeles mai bine ce se întâmplă în spatele unei relații server-client. Am aprofundat atât limbajul Python, cât și getsionarea threadurilor.
* Cred că implementarea este echilibrată, întrucât are o logică destul de ușor de urmărit.


Implementare
-

* Am implementat toate funcțiile din checker, deși ultimele 2: *state_mean_by_category* și *mean_by_category* necesită optimizare întrucât checkerul îmi da timeout cu cea propusă. Încă nu am implementat 2 din cele de tip GET.



Resurse utilizate
-

* https://ocw.cs.pub.ro/courses/asc/laboratoare/02
* [Create A Python API in 12 Minutes](https://www.youtube.com/watch?v=zsYIw6RXjfM) [1]
* https://www.geeksforgeeks.org/python-get-first-n-keyvalue-pairs-in-given-dictionary/

Git
-
1. https://github.com/dianagorescu/tema1-ASC.git

