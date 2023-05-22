# curs_vcgj_444D_flori

Am creat in Home un director git pentru clonarea repository-ului main/curs_vcgj_444D_flori:
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/128401623/86d37cfe-76c3-4b5c-ad3d-73fba40d26d1)

In git/curs_vcgj_444D_flori/app avem fisierul 444D_flori.py in care trebuie adaugat floarea aleasa, in cazul meu am ales floarea trandafir
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/128401623/e2e9ff65-2519-4dff-82f5-84532c6b9667)

In git/curs_vcgj_444D_flori/app/lib am madaugat in fisierul biblioteca_flori.py proprietatile trandafirului si anume culoare, anotimp, clasificare:


![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/128401623/e4639908-fee4-401a-bde6-bbfba6fe9b1f)

In git/curs_vcgj_444D_flori/app am rulat si testat codul din 444D_flori.py
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/128401623/14d9299f-f6b4-4372-aa98-d97c4b459468)

La sfarsitul codului in Python, pentru a rula site-ul pe localhost, vom folosi : 
app.run(host = "127.0.0.1", port = 5001) Acum vom putea porni programul 444D_flori.py din directorul /app astfel: $python3 444D_flori.py Programul va porni pe masina locala, putem accesa link-ul 127.0.0.1 :5001 SAU localhost :5001 si ne va duce pe o pagina simpla, cu un text, iar dac ape langa acest link mai punem si /lalea ne va duce catre alta pagina unde avem toate functiile cu return-urile respective.
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/128401623/f3f0ca79-ad10-4cb4-b1de-1cff4ef543f0)

! Urcarea fisierelor in serverul github am facut-o putin mai jos, la partea de jenkins


JENKINS

Pentru partea de Jenkins am creat fisierele Jenkinsfile activeaza_venv si activeaza_venv_jenkins si am atasat codurile ca atare.

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/128401623/15acc269-43a2-4e9c-b6ee-b16529785370)

Am creeat un branch personal pentru nu lucra in branchul main.

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/128401623/77e7f5dc-853f-45d4-84c0-f6fc9bc3c3c9)


Apoi am mutat fisierele pe serverul de stage cu comenzile add si commit .

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/128401623/2e556ab2-205e-4cde-8ddc-8178b946e0ea)


Inainte de a face push la aceste fisiere comise am vrut sa imi salvez credentialele in cazul in care trebuie sa urc si alte fisiere in serverul de github in viitor.

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/128401623/1ac687ad-6456-444d-9ec8-26e82afc67e1)


Am incarcat fisierele pe server cu comanda push si am instalat jenkins pe masina virtuala 


![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/128401623/b7986edb-be94-4960-a06b-a4208398d3af)


Am testat functionalitatea pipline-ului:
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/128401623/022fb1b5-d095-45e6-912e-8a838eb6df29)

Cu oceanblue:
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/128401623/fe33e507-005a-4a44-8e9a-60c3fdad283b)


















