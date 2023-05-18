# curs_vcgj_444D_flori


`Proiect site cu flori`

Pentru a face aceasta documentatie voi pune informatiile in mod cronologic.
Pentru inceput vom avea nevoie de mai multe programe instalate pe masina virtuala cu Ubuntu :
sudo apt install git(gedit,vim,python3,pytest,pip,docker,jenkins) :
Ex : instalare Docker 

![InstallDocker](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/49e6cd48-b0a5-469d-bfa8-a7b5bb05a2fa)


Fisier git/curs_vcgj_444D_flori:

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/034b8a0b-67a5-42c3-b327-9d481af9fd83)

Git status : 

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/3d683c8d-bdee-4ad7-8cbd-3f7c2c1c1512)

Fisiere proiect : 

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/660b9d75-9338-4eb6-8c15-9c749075b4a5)

Testare script-uri cu pytest:

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/93c8c4ae-5ead-4c95-920f-685b2f8fd4e5)

 
Pentru a crea acest proiect am avut nevoie de un director pe Ubuntu :
$mkdir git
	In acest director vom trage de pe GitHub un repository creat de noi.Mergem pe GitHub, intram pe contul personal, creem un repository gol in care includem un fisier README.md si un .gitignore cu template de Python.
	In CLI, dam un git status pentru a vedea daca directorul git este supervizat de git :
$git status
 
$git clone https://github.com/andrei162/curs_vcgj_444D_flori.git
$cd curs_vcgj_444D_flori
$ls -la – pentru a vedea daca s-au clonat de pe GitHub fisierele necesare pentru acest repository – README.md si .gitignore.In .gitignore am comentat linia care exclude /lib de la adaugare in git.
Acum putem crea fisierele necesare proiectului, cel mai important fiind 444D_flori.py care va face rutele si in el vom apela functiile necesare.

![ls-la](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/e0b36d53-1db9-4fd7-98c1-c216a1f4fae9)


Vom crea in /home/git/curs_vcgj_444D_flori alt director /app :
 
$mkdir app

![ls-la-app](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/54b5f31b-c407-4fa9-900d-3de870a09d89)

 
 Eu mi-am ales floarea “lalea”, deci vom avea nevoie de functiile prestabilite in model : lalea_culoare() care va intoarce string-ul “Roz” , lalea_anotimp() – care va intoarce string-ul “Primavara”, lalea_clasificare() – care va intoace string-ul “Liliaceae”.

Vom crea inca un director in /home/git/curs_vcgj_444D_flori/app - /lib
$mkdir lib

![ls-la-lib](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/ba27905e-7929-4d3a-8ff7-7afe65c0a114)
 
	`In acest fisier vom pune biblioteca care va descrie functiile pe care le vom folosi in fisierul 444D_flori.py`
$touch biblioteca_flori.py
$gedit biblioteca_flori.py
	Aici vom scrie functii ca in exemplul de mai jos :
  
  ![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/fcf4a644-60dc-4187-bdac-a775c8221e04)
 
Creem fisierul 444D_flori.py in directorul /home/git/curs_vcgj_444D_flori/app
Pentru a crea un fisier python folosim :
$touch 444D_flori.py
$gedit 444D_flori.py / vim 444D_flori.py  - 444D_flori – numele fisierului, .py – extensia
	Pentru ca vrem sa lucram pe un branch separat, folosim git branch pentru a vedea pe ce branch suntem, theoretic suntem pe branch-ul main sau master. Vom crea un nou branch :
$git branch devel/andrei162_flori

![branch_devel](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/6586808e-60a5-4d55-acf3-e90dbde49e3e)
 
$git checkout devel/andrei162_flori – Schimbam branch-ul pe care suntem (main) pe cel creat mai sus.
	Pentru fiecare route folosim :
@app.route
	Exemple de rute + functie pentru a crea un link : 
  
  ![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/b47b7e34-4bcf-4b9c-aa68-a973b713dd01)
  
  ![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/46fcace6-9ba9-4c7d-b77f-2210e9a9155c)
  
  
 
	La sfarsitul codului in Python, pentru a rula site-ul pe localhost, vom folosi : 
app.run(host = "127.0.0.1", port = 5001)
	Acum vom putea porni programul 444D_flori.py din directorul /app astfel:
$python3 444D_flori.py
	Programul va porni pe masina locala, putem accesa link-ul 127.0.0.1 :5001 SAU localhost :5001 si ne va duce pe o pagina simpla, cu un text, iar dac ape langa acest link mai punem si /lalea ne va duce catre alta pagina unde avem toate functiile cu return-urile respective.
  
![lalea_docker](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/0d8025df-7c4d-45fc-ab5c-a26845401d44)  

![lalea_culoare_docker](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/dbdb4d40-d492-42db-81f8-a37b78437031)

![lalea_anotimp_docker](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/d55e44ad-8112-4b8a-a851-a48109dc56d7)

![lalea_clasificare_docker](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/dd796aa8-486f-4cd8-a595-a11e0584c0ed)


	In directorul /app vom mai face un director cu numele tests :
$cd ../
$mkdir tests
	Aici vom crea fisierul test_biblioteca_flori.py si vom crea niste functii de testare cu if,else : 
 bflori este fisierul importat din /lib – biblioteca_flori.py
	Pentru a vedea daca merg testele, instalam pytest : 
$sudo apt install pip
$pip install pytest
	Pentru a rula testele local - pytest, folosim comanda (pentru python 3.10):
$python3 -m pytest

![pytest](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/d80c9ead-27e2-4d9e-bfff-6252a4046fff)
 
	Pentru ca modificarile aduse repository-ului sa fie trimise pe serverul remote – pe GitHub va trebui sa dam comenzile urmatoare din directorul /home/git/curs_vcgj_444D_flori :
$git status

![git_status](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/08f3d559-8c70-4d62-b51a-2953fa2e34d1)

$git add . / $git add * - pentru a adauga toate fisierele existente in commit pe branch-ul curent
$git commit -m “Modificare/Adaugare/Stergere fisierele a,b pentru motivele c,d »

![git_commit](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/d7139778-c26b-446a-a426-a2efce37f358)

	In acest moment avem totul pregatit pentru a urca pe repository-ul remote, dar git-ul nu va sti unde sa incarce si nici nu cunoaste branch-ul creat de noi, deci va trebui sa configuram git-ul astfel :
$git config –global user.email(mail@domain.x)
$git config –global user.name(name)
$git config –credentials.helper store 
$git push – moment in care CLI ne va cere username-ul de pe git : andrei162 in cazul meu, si parola care consista intr-un token pe care il obtinem astfel : 
Intram pe GitHub, la setari , developer options, create token (classic) , token-ul este de tip hash – il salvam undeva secret si il introducem la parola in CLI, iar credentialele noastre vor fi salvate pentru acest repository.

![git_push](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/a0944d8c-92e2-4a9f-b12c-ed41c0a24b8f)
	
In acest moment, branch-ul nostrum va fi urcat pe GitHub cu tot proiectul nostrum si putem trece la partea de testare.
 
	Vom avea 6 teste in fisierul test_biblioteca_flori.py – culoare crin,lalea – anotimp crin,lalea – clasificare crin,lalea.
Alte comenzi utile pentru git :
$git config –global alias.hist “log –oneline –graph –decorate –all” – ne creeaza o noua comanda pe care o apelam astfel : $git hist ; - ne va afisa istoricul branch-urilor si al commit-urilor.
$git config –global --list


`Testare Jenkins`


Acum avem nevoie de testare cu Jenkins. Pentru a instala Jenkins trebuie sa urmam niste pasi :
1.Verificare daca este instalat java : $java -version
	2.Instalare Java : $sudo apt install java
	3.$sudo apt install openjdk-11-jdk  - pentru JavaJDK 11
	4.$sudo apt install curl
	5.$curl -fsSl <JenkinsURL> | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
	6.$echo deb [signed-by=/usr/share/keyrings/Jenkins-keyring.asc] <jenkins Package URL> binary | sudo tee /etc/apt/source.list.d/Jenkins.list > dev/null
	7.$sudo apt-get update
	8.$sudo apt install jenkins -y
	9.$sudo systemctl status Jenkins
  
  ![status_jenkins](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/24b71d32-0754-49b6-b1f0-78a0111ab532)
 
	Accesam localhost:8080 pe browser.
	De aici va porni sistemul Jenkins – Prima data ne va cere Administrator password.Pentru aceasta va trebui sa accesam un fisier secret din calea urmatoare : 
$sudo cat /var/lib/Jenkins/secrets/initialAdminPassword – ne va da in consola CLI parola de tip hash pe care o introducem in Jenkins.
De aici vom configura contul de Jenkins care se ocupa de acest repository si de aici putem crea teste pentru script-uri – Freestyle,Pipeline
Install suggested Plugins 
Create account -> user = admin ; password = admin -> Save and Continue -> Manage Jenkins -> Install Plugins -> Available Plugins -> Search Blue Ocean -> Install 
 
Pentru testare automata cu Jenkins pipeline, vom avea nevoie de Jenkinsfile :
$touch Jenkinsfile  
  
 ![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/d706dc5a-0589-4643-aa33-03dc0b3ad8a7)
 
 -exemplu de stage – Testare pylint:
  
  ![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/eb41ef80-442c-4f09-be4e-efc4c2582ec9)
  
	Pentru a rula automat, Jenkins-ul are nevoie de un Virtual Environnement si de requirements – programme cerute pentru a putea rula in venv.Un venv va fi local – activeaza_venv, iar celalalt pentru Jenkins pe server – activeaza_venv_jenkins.De asemenea, pentru a rula aplicatia pe server avem nevoie de alt fisier ruleaza_aplicatia.
$touch quickrequirements.txt – in /app
  
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/369760a1-ab22-449a-8a89-e0b0b7af5dc6)
 
$touch activeaza_venv 
  
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/2bf41e20-b1b1-4476-a189-d7b1bdc0ebf4)
 
![activeaza_venv](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/de0a623e-e8e7-4f94-8197-e5b5f4d2bb6b)
 
$touch activeaza_venv_jenkins
 
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/fddcf32b-7e14-4804-b088-6950a301e042)

$touch ruleaza aplicatia
 	
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/649791c4-3de6-4daf-81d6-9d27496cea18)

-	Aplicatia va rula acum pe portul 5011.
Fisierul Jenkinsfile va activa virtual environment-ul pentru Jenkins si va da build la program si va rula testarile : pylint, Unit Test -  pytest 
  
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/d65d7147-956a-4fdf-8b6b-94067d7347c8)
 
	In browser, pe Jenkins – configuram Jenkins-ul astfel incat sa folosim un plugin – Blue Ocean care ne creaza o interfata unde vedem o diagrama cu toate stage-urile aplicatiei de test si astfel vedem eventuale erori – Jenkins-ul ne va spune unde si ce anume a picat si mesajele noastre din fisierul Jenkinsfile(daca exista).
  
	Pentru a rula testarea automata cu Jenkins trebuie sa dam New Build, ii dam un nume,selectam Pipeline, selectam la Script -> Script from SCM - > Select SCM -> GitHub -> GitHub Repository URL -> Select branch -> /devel/andrei162_flori – selectam branch-ul pe care am lucrat -> Save.
  
![scm_jenkins](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/c0eae3cd-e93f-4da5-ab50-4aad0de4a154) 
 
	Urmatorul pas este sa apasam Build -> Se va crea build-ul cu toate stage-urile existente in Jenkinsfile, iar daca apasam pe Open Blue Ocean -> Vom vedea diagrama cu etapele.
  
  ![jenkins_pipeline_bo](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/336a78f7-eb17-400e-b001-4b1630f88a37)
  
![jenkins_project](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/43288e4e-3070-4de3-9cd6-fae79e56732d)
  
	Daca modificam ceva in cod sau stergem/adaugam/modificam fisiere, va trebui urcat pe git astfel : 
$git status
$git add <filename> SAU $git add . SAU $git add *
$git commit -m “message”
$git push
 
	Astfel, cand dam iar Build in Jenkins, va lua iar repository-ul de pe GitHub si va rula cu noile modificari aduse in repository.

Containerizare cu Docker
	
	Pentru containerizare folosim serviciile Docker – punem aplicatia cu toate dependintele si virtual environment pentru a putea rula intr-o « cutie » si nu pe masina noastra locala.
	Pentru inceput, instalam docker :
1.sudo apt-get update
2.sudo apt-get install ca-certificates curl gnupg lsb-release
3.sudo mkdir -p /etc/apy/keyrings
4.curl -fsSL <DockerURL> | sudo gpg –dearmor -o /etc/apy/keyrings/docker.gpg
4.echo “deb [arch=$(dpkg –print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] <DockerURL> $(lsb_release -cs) stable”| sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
5.sudo apt-get update
6.sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin docker-compose
	Pentru a face acest lucru avem nevoie de un Dockerfile, o imagine cu nume – 444D_flori, un fisier pentru a porni serviciul docker – dockerstart.sh
Continut repository : 

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/097ff807-e690-4d52-b29d-97d3726f4a48)

Dockerfile pentru aplicatie Flask in Python 3 :
 
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/7a55cf5d-2524-4404-84a5-b6354cb2e6df)
  
Continut /app :
  
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/b83498ec-e752-4e55-bd3f-45a1dd51aca5)
 
Dockerstart.sh : 
  
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/0ebafd18-d08b-4365-b395-79fdec2832f0)

 
Pentru a crea imaginea, dam comanda in CLI : 
$sudo docker build -t 444d_flori:v01 .
 
 ![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/f242e118-0a2c-4a2f-bc2a-e46d78d8c88f)

O putem vedea folosind comanda :

$sudo docker images

 ![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/1088c1a5-ebf0-4b37-9a9a-f5ae267f731d)

 
Pentru a rula containerul pe Docker, folosim comanda :

$sudo docker run --name 444D_flori -p 8020:5001 444d_flori:v01 
8020 – portul de pe masina locala unde va raspunde serverul din docker 
5001 – portul din interiorul containerului
444d_flori – numele containerului
444D_flori – numele repository-ului
:v01 – versiunea pentru container
  
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/292643af-010d-4bd5-a69c-92a906d78ce9)
 

Pentru a rula in background containerul – adaugam -d in comanda de rulare a containerului.

Comenzi utile :

$sudo docker ps -a – Arata toate imaginile create si repository
  
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/267715a7-3c25-4124-a685-eabcaaa90015)

$sudo docker start <nume container> - comanda de start a unui container 
$sudo docker stop <nume container> - comanda de stop a unui container

$sudo docker rm <nume container> - comanda de stergere a unui container
$sudo docker rmi <id_imagine> - comanda de stergere a unei imagini
 

$sudo docker export <imagine> > <arhiva.tgz> - export imagine pe DockerHub
$sudo docker import <arhiva>) – import imagine de pe DockerHub


$docker login – ne conecteaza la contul de DockerHub
$docker tag nume_docker_tag <nume imagine> <username>/<nume_imagine> - adaugare tag pentru o imagine
$docker push <username>/<nume_imagine> - incarcare container pe DockerHub
$sudo docker attach – dupa run – ne activeaza request-urile pentru containerul care ruleaza – de exemplu accesam site-ul de flori – ne va afisa in consola request-ul


`Creare Pull Request:`
  
![PR_reviews_required](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/1728c804-4b51-4f6a-a7b2-5a964ed5508a)
  
Link PR :  Devel/andrei162 flori #2 : https://github.com/andrei162/curs_vcgj_444D_flori/pull/2

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/127126771/cee70124-e9e8-4e65-b629-f58319d80819)




