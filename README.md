# curs_vcgj_444D_flori

Proiect site flori- GHIOCEL

Am instalat pe masina virtuala python3, pytest, jenkins, docker, git, gedit

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/047593c7-ce42-4117-a708-1e5aabd8f2e8)
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/fbee8eaf-8214-4f52-9f80-9fa488ac95f8)
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/c3b83123-e775-414a-af18-65f8b6a2339b)
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/901c675a-c6ad-4bbe-ab29-11eeb0dbb85e)
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/4997eeb2-6c7a-45b8-86a6-ee1a7de20355)
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/736d52e0-eeac-416d-bcda-95015e15fdec)

Fisier git/curs_vcgj_444D_flori si fisierele proiect:
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/33b7867d-c5ba-40b3-92b3-bb617678239a)

Tesatarea script-urilor cu ajutorul comenzii pytest:
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/5f9dbb76-5da9-4850-8335-ac8b5be6e4aa)


In fisierul director denumit lib se afla biblioteca in care descriem functiile folosite
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/c6fbd26b-d062-4073-a200-8f7d34fef2b3)

Functiile folosite:
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/f63c3291-23e8-4422-83ae-ec6da5a83caa)

Pentru a crea un fisier python folosim : $touch 444D_flori.py $gedit 444D_flori.py / vim 444D_flori.py - 444D_flori – numele fisierului, .py – extensia. Pentru ca vrem sa lucram pe un branch separat, folosim git branch pentru a vedea pe ce branch suntem, theoretic suntem pe branch-ul main sau master. Vom crea un nou branch : $git branch devel/danielatoh_flori.

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/7a840b3a-e7fe-4b18-9ef2-74f2d984dae5)

Programul 444D_flori.py
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/3df8cb35-b819-4333-b75d-1a7e7ba8b388)
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/1faa2691-d84f-4ccd-97ce-2480f7d35fe2)
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/d14a8c98-8708-4cf6-85ac-a7dfb3ee8d09)
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/bdb2dfbd-0acd-47db-b07f-b195705c944b)

In fisierul test_biblioteca_flori.py am creat fisierul test unde am implementat functiile if si else pentru a verifica programul

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/d524d165-e8e4-4583-a4cf-9a14acfd7c3a)

Deoarece modificarile aduse repository-ului nu se salveaza automat si nu se trimit pe serverul remote, ne aujatm de urmatoareale functii:
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/e10f1f48-d463-4ae4-81f4-d82a185baece)

si de functia $git commit -m “Modificare/Adaugare/Stergere fisierele a,b pentru motivele c,d »

GIT-ul este configurat cu ajutorul comenzilor de mai jos, deoarece el nu cunoaste brach-ul creat de noi in mod implicit
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/bc66ea81-91f1-4f74-a1b9-d2ab20c0f5cf)

Token-ul este de tip hash – il salvam undeva secret si il introducem la parola in CLI, iar credentialele noastre vor fi salvate pentru acest repository.

In urmatoarea etapa vom face testarea proiectului
Testare Jenkins
Pentru a instala Jenkins trebuie sa urmam niste pasi : 
1.Verificare daca este instalat java : $java -version 
2.Instalare Java : $sudo apt install java 
3.$sudo apt install openjdk-11-jdk - pentru JavaJDK 11 
4.$sudo apt install curl 
5.$curl -fsSl | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null 
6.$echo deb [signed-by=/usr/share/keyrings/Jenkins-keyring.asc] binary | sudo tee /etc/apt/source.list.d/Jenkins.list > dev/null 
7.$sudo apt-get update 
8.$sudo apt install jenkins -y 
9.$sudo systemctl status Jenkins

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/788908b9-d137-42fc-9279-b8f7eb372f06)

Tesatre pylint:
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/38bb0933-09c3-45be-9872-ab8b459c8c15)

$touch quickrequirements.txt – in /app
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/ac1cebbe-5970-4f48-a71a-f97495df71ee)

$touch activeaza_venv
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/f52af1a5-40f7-4ca6-9d73-f1fe9b1fde32)
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/957c229d-fa33-4aff-897c-d28020cff91d)

$touch activeaza_venv_jenkins
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/3cd62403-f66e-4e5f-af30-5bb658e709c3)

$touch ruleaza aplicatia
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/29957d44-fae1-4b23-9fa0-fdbf5fe6f8bc)

Aplicatia va rula acum pe portul 5011. Fisierul Jenkinsfile va activa virtual environment-ul pentru Jenkins si va da build la program si va rula testarile : pylint, Unit Test - pytest
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/dcfe6200-68bc-44d7-b7b4-381aa071a423)

In browser, pe Jenkins – configuram Jenkins-ul astfel incat sa folosim un plugin – Blue Ocean care ne creaza o interfata unde vedem o diagrama cu toate stage-urile aplicatiei de test si astfel vedem eventuale erori – Jenkins-ul ne va spune unde si ce anume a picat si mesajele noastre din fisierul Jenkinsfile(daca exista).
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/b7af5050-ccab-4f6d-b8b6-78477723e9e9)
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/12c71c1d-7ec3-4b3d-b644-c3f14dc3b325)

Containerizare cu Docker

Pentru containerizare folosim serviciile Docker – punem aplicatia cu toate dependintele si virtual environment pentru a putea rula intr-o « cutie » si nu pe masina noastra locala.
Pentru inceput, instalam docker:

1.sudo apt-get update 
2.sudo apt-get install ca-certificates curl gnupg lsb-release
3.sudo mkdir -p /etc/apy/keyrings 4.curl -fsSL | sudo gpg –dearmor -o /etc/apy/keyrings/docker.gpg 
4.echo “deb [arch=$(dpkg –print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] $(lsb_release -cs) stable”| sudo tee /etc/apt/sources.list.d/docker.list > /dev/null 
5.sudo apt-get update 
6.sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin docker-compose Pentru a face acest lucru avem nevoie de un Dockerfile, o imagine cu nume – 444D_flori, un fisier pentru a porni serviciul docker – dockerstart.sh Continut repository:

Dockerfile pentru aplicatie Flask in Python 3:
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/5d473db8-e074-4418-9e71-99d4ebe0fbf9)

Continut /app:

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/adc8fa2e-9608-4c36-a335-d2bfe9a26422)

Dockerstart.sh:

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/8833e8cc-7bc0-4b0f-91c7-ab2758c671eb)

Cu ajutorul comenzii de mai jos putem sa cream imaginea:

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/231cbd64-6db0-4389-8cf2-242379e4194a)

Aceasta imagine se poate vedea utilizand urmatoarea comanda:

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/67d1c43d-3e25-4de5-bbd1-87f3bb878111)

Pentru a rula containerul pe Docker, folosim comanda :

$sudo docker run --name 444D_flori -p 8020:5001 444d_flori:v01 8020 – portul de pe masina locala unde va raspunde serverul din docker 5001 – portul din interiorul containerului 444d_flori – numele containerului 444D_flori – numele repository-ului :v01 – versiunea pentru container

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/efebe623-f7f1-4721-a3bb-c36e0c115eea)


In fisierul uau.txt se afla toate comenzile folosite in realizarea acestui proiect
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/132925764/5c891bd1-318c-4a72-a5d7-8023f102e1ea)
