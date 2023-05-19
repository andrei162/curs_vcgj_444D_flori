# curs_vcgj_444D_flori
## Floarea aleasa: camelia
#### Balan Andreea-Daniela 444D

Am instalat toate programele de care voi avea nevoie in realizarea proiectului (Jenkins, git, Docker) in timpul laboratoarelor. Am instalat si dependinetele care lipseau utilizand comenzile urmatoare:
```
    sudo apt install python3-pip
    pip install pytest
    sudo apt install gedit
    pip install flask
    sudo apt install python3-venv
```

Am clonat repository-ul de pe github:
```
git clone https://github.com/andrei162/curs_vcgj_444D_flori.git
```

Pe desktop s-a creat directorul corespunzator repository-ului creat:

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/82381145/49009382-2cdf-4b4b-9484-a5074defdcea)

Putem vizualiza si fisierele din interiorul lui:

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/82381145/4d152b46-255d-4202-8f85-5020fb046e06)

In directorul app exista urmatoarele fisiere:

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/82381145/1a946ef5-571c-40f2-b720-f432ffb7ae99)

Am creat un branch nou numit *devel/AndreeaBD_flori* cu comanda *git branch* si m-am mutat pe noul branch cu comanda *git checkout*.

Fisierul ***444D_flori*** contine toate metodele de GET si POST din aplicatia noastra. Aici se face redirectionarea catre paginile specifice fiecarei functii si cereri implementate in proiect. Voi edita fisierul cu *gedit* si voi adauga functionalitatile corespunzatoare florii alese. Eu am ales camelia cu caracteristicile: culoare-roz, anotimp-primavara, clasificare-Camellia Japonica.

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/82381145/2f484388-509a-47af-bd53-5397dc0197ab)

In fisierul ***biblioteca_flori.py*** din *lib* sunt definite functiile care returneaza caracteristicile fiecarei flori. Am adaugat functiile pentru camelie:

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/82381145/bb77abc9-f417-4688-9a0b-05bf3ee470ee)

In folderul *tests* exista si un fisier numit ***test_biblioteca_flori.py*** in care sunt implementate teste pentru verificarea functionarii corecte a aplicatiei. In fiecare test am setat parametrul care ar trebui sa fie returnat de functiile definite in ***biblioteca_flori.py*** si am verificat daca acesta corespunde cu ceaa ce returneaza functiile de fapt:

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/82381145/2c306b6b-1cd7-41b5-a994-6f78ebe0a0ab)

Pentru a rula testele am folosit comanda:
```
python3 -m pytest ./tests -v
```
    
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/82381145/f48371bd-3a92-4736-9e4c-6f66ea93af28)

Voi porni aplicatia utilizand comanda:
```
python3 444D_flori.py
```

Aceasta functioneaza pe portul 5001 deci in browser voi intra pe *localhost:5001* unde ar trebui sa fie index-ul aplicatiei adica pagina de start:

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/82381145/4c384e17-70aa-4227-8ebd-eefce9d26e9d)
 
 Voi verifica daca toate paginile exista si sunt functionale:  /camelie/culoare,  /camelie/anotimp si  /camelie/clasificare. Pentru a face asta, voi merge intai pe pagina corespunzatoare florii alese de mine: /camelie.
 
 ![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/82381145/15c4cb99-b1a6-478a-a4bb-b409eda94979)

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/82381145/8917c0b6-87a3-4725-94c6-bd737fb4ab14)

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/82381145/bf730576-dee0-4e7b-925d-266c0e6ba624)

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/82381145/b11d7c23-a738-4308-b540-3713351c613e)

In terminal putem vedea si metodele de GET apelate din scriptul de python:

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/82381145/7c8a4183-53cc-482e-8af3-29f46b862b98)

Pentru a configura pipeline-ul de Jenkins am intrat pe *localhost:8080* si am creat un cont cu token-ul generat in github. DIn *maange jenkins*/*install plugins*/*available plugins* am instalat *Blue Ocean*. Din meniu am accesat *new item* si am creat un pipeline pe repository-ul clonat, pe branch-ul meu. Legatura cu server-ul se face in fisierul *Jenkinsfile* din repository.

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/82381145/6f220daa-d979-4487-babc-ae604e59b16f)

Am rulat pipeline-ul si testele de jenkins au trecut:

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/82381145/b9dca45a-3a6a-4b00-a8ba-47d49f5f2149)

In fisierul 444D_flori.py comentez ultima linie care se ocupa de rularea aplicatiei pe portul specificat in localhost pentru ca vom porni aplicatia din docker:

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/82381145/c838848a-8f31-4f23-8386-3e70c841ce28)

Configuratia pentru docker se afla in fisierul *Dockerfile*.
Pentru a crea imaginea de docker si a rula container-ul am folosit comenzile:

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/82381145/c640e083-44ab-4da5-8e5b-a501131a53a5)

Daca accesez acum aceleasi pagini pe care le-am testat in localhost:5001 si pe portul *http://172.17.0.2:5020/* unde ruleaza docker, voi obtine acelasi continut, adica aceleasi pagini definite in scriptul de python.

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/82381145/6f8d4d57-0388-4a84-bab5-908a1605e161)

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/82381145/5d875905-212f-475d-8871-03aa4449d4b0)

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/82381145/8bec87e3-7589-44e6-89b2-a7a7827f2003)

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/82381145/75737be6-c037-4d28-b56f-104bbe885157)

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/82381145/09fedc20-14ff-4d60-9811-ba92af7e8b24)

Pentru a urca modificarile facute in fisiere pe github, am rulat comenzile:
```
git add .
git commit -m
git push
```
Exemplu:

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/82381145/31407ba6-7da5-48c9-a6bd-848c18a0d3a1)

Cu *git status* am verificat ce fisiere se afla in staging si ce fisiere au modificari care nu au fost commited.

In final am facut un pull request:



