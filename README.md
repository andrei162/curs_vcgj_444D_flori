# curs_vcgj_444D_flori
Mentionez de la inceput ca mie mi s-a inchis terminalul si singura metoda de a recupera ce am facut este folosind comanda history
Voi adauga doar cod si ulterior voi reface anumite parti in terminal.
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

Cu change directory trecem in app directory unde se va crea un fisier gol quickrequirements.txt .
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




