# curs_vcgj_444D_flori
Mentionez de la inceput ca mie mi s-a inchis terminalul si singura metoda de a recupera ce am facut este folosind comanda history
Voi adauga doar cod si ulterior voi reface anumite parti in terminal.
Trebuie sa avem instalate mai multe programe cu comanda sudo apt install dar mai intai, pentru a crea acest proiect, avem nevoie de un director pe Ubuntu. Folosim comanda mkdir dir-local GIT,pentru a crea directorul in care vom incarca de pe GitHub un repository creat de noi din contul de GitHub. Cu git status verificam starea directorului.
Cu comanda ls -la data in directorul curs_vcgj_444D_flori vedem:
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/93121932/eaafa8d3-b750-46eb-8f77-49ab1221ad91)
Si tot cu comanda ls -la data in directorul app vedem:
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/93121932/8a75a6b8-f253-407e-8d0d-4cf0aa8aa27b)
Pentru floarea aleasa de mine,"bujor", este nevoie de cele 3 functii bujor_culoare() care trebuie sa afiseze "Rosu", bujor_anotimp() afiseaza "primavara" si bujor_clasificare() care afiseaza "parfumat"
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/93121932/5c377840-c963-48ba-84a1-0159040ec0bb)
Cum se observa in imaginea de mai sus, in directorul lib se va regasi bibioteca care va descrie functiile de mai sus.
Cream fisierul biblioteca_flori.py cu touch, copiem continutul folosindu-ne de gedit si salvam.
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/93121932/2b3ff1ab-a53b-4a5b-9247-1b8973c8b2b1)
La fel si pentru fisierele Jenkinsfile, afiseaza_venv, afiseaza_venv_jenkins si ruleaza_aplicatia:
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/93121932/cd6e1ea2-0903-4ffb-acd0-0cfe5ee4b9d0)
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/93121932/bc515ccb-69d8-47ad-9e11-cb5eee2b9e53)
Se creeaza un fisier de tip python, 444D_flori.py unde adaugam cpd pentru floarea aleasa:
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/93121932/2f587328-ec7e-47c9-8c4a-a5aec7ba9829)
Aplicatia ruleaza la portul 5001 la adresa IP 127.0.0.1. Accesam prin browser http://127.0.0.1:5001/bujor/ dupa ce am dat comanda in Terminal :
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/93121932/6ab9459b-edd1-4753-8b73-2ea7ec687586)
In continuare, se creeaza un nou alt director cu numele tests unde vom crea testul pentru biblioteca noastra. Testul consta in mai multe functii pentru culoare, anotimp si clasificare pe care biblioteca_flori trebuie sa le treaca.

Avem nevoie de testare cu Jenkins. Pentru a instala Jenkins trebuie sa urmam niste pasi : 
1.Verificam daca este instalat java : $java -version 
2.Instalam  Java daca este nevoie : $sudo apt install java
4.$sudo apt install curl 
5.$curl -fsSl | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
6.$echo deb [signed-by=/usr/share/keyrings/Jenkins-keyring.asc] binary | sudo tee /etc/apt/source.list.d/Jenkins.list > dev/null 
7.$sudo apt-get update 
8.$sudo apt install jenkins -y 9.$sudo systemctl status Jenkins
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/93121932/79552d56-9575-4daa-aeb2-b492346baa60)

Pentru curs_vcj_44D_flori/, folosim comanda  sudo apt-get update pentru a pune la dispozitie ultimele informatii din repository -urile configurate si comanda  sudo apt-get install ca-certificates curl gnupg lsb-release care instaleaza ce a fost specificat :ca-certificates, curl, gnupg, lsb-released folosind apt-get(manager pentru package)
Docker download:
Se descarca cheia GPG pentru repository-ul Docker si se salveaza ca un fisier docker.gpg intr-un directory folosind comanda: curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg.
Se configureaza  fisierul docker.list si se foloseste comanda tee pentru a scrie outputul si in fisier si in consola: echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
Folosim iarasi comanda sudo apt-get update pentru a updata lista astfel incat sa se includa repository-ul pentru Docker adaugat in pasii de mai sus.
Prin comanda sudo chmod 777 /etc/apt/keyrings/docker.gpg obtinem permisiunea ca fisierul docker.gpg sa poata fi citit, scris si executat
Cu comanda sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin docker-compose se instaleaza Docker-ul si pachetele sale: docker-ce, docker-ce-cli, containerd.io, docker-compose-plugin, and docker-compose
Se creeaza cu comanda touch Dockerfile un fisier gol cu numele Dockerfile pe care il punem deschide pentru a edita cu comanda gedit Dockerfile:
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/93121932/c1fd8e0c-920b-4a7d-a970-4c9cbeaf151e)


![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/93121932/5f18fbbb-69cd-4725-a467-af7a5a09c09b)

Cu change directory trecem in app directory unde se va crea un fisier gol quickrequirements.txt.
cd app
touch quickrequirements.txt
gedit quickrequirements.txt -> comanda cu care deschidem si editam fisierul quickrequirements.txt :
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/93121932/19fa2312-e94a-4f27-97a2-c886a2eac305)
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/93121932/e98d2f3c-4ed1-42d9-9a3f-10579e7a6c53)

La fel si pentru dockerstart.sh: 
touch dockerstart.sh
gedit dockerstart.sh
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/93121932/0646e6bf-47c3-44df-8327-c4edd766091e)
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/93121932/2695ead9-1aed-4d87-83c7-5e02568f77cc)
Pasul urmator, dupa ce ajungem in directorul parinte, este sa definim o imagine Docker cu numele 444d-flori:v01 (d-ul este mic intrucat face parte din denumirea unei imagini) folosindu-ne de Dockerfile : sudo docker build -t 444d_flori:v01 .
Intram in directorul app si activam cu comanda source activeaza_venv, mediul activeaza_venv ale carui variabile vor fi disponibile.
Se defineste inca o imagine ca cea de mai sus cu aceeasi comanda.
Cu comanda sudo docker images se vor afisa toate imaginile Docker disponibile in sistem iar cu comanda sudo docker ps -a  vom afisa lista cu containerele Docker.
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/93121932/fa666c2f-b9ac-48a8-835f-2ce248bf9b61)

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/93121932/76a41abc-13e2-4b38-aa13-3966cc431696)

sudo docker run --name 444d_flori -p 8020:5020 444d_flori:v01 -> ruleaza  container-ul 444d_flori si asociaza port-ul 5020 cu portul 8020. 
In continuare se vor afisa absolut toate containerele Docker: sudo docker ps -a.
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/93121932/400e13bc-9a4f-4bcf-930b-77021c1f8f5c)
Folosindu-ne de container id , utilizam comanda sudo docker rm 794e26e1e590:
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/93121932/3f9ae76c-f509-45d4-bb75-37187b84aa80)
Comanda sudo docker:
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/93121932/6bea35b4-8fce-4a8a-abfb-9eacb599d616)


