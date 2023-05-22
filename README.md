# curs_vcgj_444D_flori

Crusitu Ioan-Teofil 444D 

Floare: Hortensie


Pentru inceput am facut niste verificari " de rutina" prin comanda _sudo apt get update_ si verificari la nivelul aplicatiilor python3, gedit, git si altele, pentru a vedea daca sunt sau nu instalate si gata de utilizare. (ex: _sudo apt install python3_)
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/103361643/8f37ac57-7249-49b9-8875-5b0e297b043b)

De asemenea am descarcat si Flask-ul cu ajutorul urmatoarei comenzi:
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/103361643/aabf4102-d9ee-49dc-83a2-2a20607ad38a)

Dupa ce am facut aceste mici verificari am inceput sa facem primele modificari in fisierul biblioteca_flori.py din /app/lib adaugand hortensia (floarea pe care eu am ales-o) in biblioteca.

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/103361643/490cbedf-45d3-442c-ac44-05e91d5c752c)

Umatorul pas a fost sa introduc in directorul de teste din /app in fisierul test_biblioteca_flori.py floarea pe care eu am ales-o.

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/103361643/9c101956-3c23-46cd-8ce7-e3ab558844be)

Un ultim pas a fost sa adaugam rutele in /app 444D_flori.py o sa putem testa local aplicatia.
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/103361643/25b8260c-c0bb-40e9-8360-b8a56fcc0b0a)

Acum pentru a verifica ceea ce am facut, am folosit comanda _python3 444D_flori.py_

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/103361643/376bf528-d9c6-4818-b5a4-0a2cefd93106)

De unde am luat adresa localhost-ului si am adaugat la final _/hortensie_

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/103361643/fef307bd-dee1-4354-baa4-6dc6d1c96ea2)

Pentru o vizualizare mai exacta putem folosi urmatoarea comanda 
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/103361643/732766f5-5b2d-4759-96e7-ac9623c9b661)

Mai departe creez in /app fisierele activeaza_venv, activeaza_venv_jenkins si ruleaza_aplicatia si fisierul pipeline Jenkinsfile pentru a putea testa aplicatia online cu Jenkins.
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/103361643/080055b0-0ee6-49bf-9104-a9a61a9eb8a5)

Creez un branch de developer local pentru a nu modifica aplicatia principala cand voi da push pe git. 

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/103361643/217b7659-db6e-4901-8050-f4f483bca0b8)

Schimbam branchul pe cel creat mai devreme.

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/103361643/4863437e-c465-4274-8132-f22487685d6b)

Dupa asta, folosim git add pentru adaugarea modificarilor pe branch si ulterior git commit.

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/103361643/3ab96c6f-e22b-48b4-abfa-9cb20b52f5c8)


Dupa build aplicatiei de pe branchul devel are succes. Se poate folosi si Blueocean pentru mai multe detalii ale buildului de pipeline.

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/103361643/4a805a2d-aac4-4a31-9b75-26752eed8712)

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/103361643/fa863762-f1e8-453f-9d9e-5919dc68aaba)




