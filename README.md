# curs_vcgj_444D_flori

Proiect site cu flori

Pentru inceput vom avea nevoie de mai multe programe instalate pe masina virtuala cu Ubuntu : git, gedit,vim,python3,pytest,pip,docker,jenkins
Status git:
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/84671601/bd001251-11f6-4276-aa40-c25ec91b875c)

Fisiere proiect:
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/84671601/4283b9b0-69dd-4f25-9ca3-358eb09623f7)

Pentru a crea acest proiect, avem nevoie de un director pe Ubuntu: $ mkdir git În acest director, vom extrage un depozit pe care l-am creat din GitHub. Mergem la GitHub, intrăm în contul nostru personal și creăm un depozit gol cu un fișier README în el. md și .gitignore cu șabloane Python. În CLI, dăm o stare git pentru a vedea dacă directorul git este supravegheat de git: $git status

$ git clone https://github.com/andrei162/curs_vcgj_444D_flori.git $ cd curs_vcgj_444D_flori $ ls -la - pentru a vedea dacă ați clonat fișierele necesare pentru acest depozit din GitHub - README.md și .gitignore.In . /lib comentat este adăugat la linia git. Acum putem crea fișierele necesare pentru proiect, cel mai important 444D_flori.py, care va genera rutele, unde vom apela funcțiile necesare.

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/84671601/a173878a-35c9-4b8f-aa5e-e13ff2733d42)
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/84671601/28242138-4294-4661-b4aa-bdddfc502123)
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/84671601/cd1d6cdb-7974-44a8-9294-ffe9a215475f)
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/84671601/701a2846-f650-4dd6-91fa-1192bbcd4dbe)

La sfarsitul codului in Python, pentru a rula site-ul folosind localhost-ul, vom folosi: 
app.run(host = "127.0.0.1", port = 5001) Acum vom putea porni programul 444D_flori.py din directorul /app astfel: $python3 444D_flori.py Programul va porni pe masina locala, putem accesa link-ul 127.0.0.1 :5001 SAU localhost :5001 si ne va duce pe o pagina simpla, cu un text, iar dac ape langa acest link mai punem si /lalea ne va duce catre alta pagina unde avem toate functiile cu return-urile respective.

Rezultatele testarii:
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/84671601/1dd334f1-eef7-47c9-9b27-1e52c937fe49)

Instalare Jenkins:
1.Verificare daca este instalat java: $java -version
2.Instalare Java : $sudo apt install java
3.$sudo apt install openjdk-11-jdk - pentru JavaJDK 11
4.$sudo apt install curl
5.$curl -fsSl | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
6.$echo deb [signed-by=/usr/share/keyrings/Jenkins-keyring.asc] binary | sudo tee /etc/apt/source.list.d/Jenkins.list > dev/null
7.$sudo apt-get update
8.$sudo apt install jenkins -y
9.$sudo systemctl status Jenkins
Status Jenkins:
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/84671601/651cf252-3bb4-4fa4-b1e6-25d58659aa92)

Test Jenkins:
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/84671601/76c8d97e-a96a-4bd4-b8e3-38a51760d756)
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/84671601/cc4a0dfe-3184-484b-a037-617b9f315b26)


Accesand localhost:8080, va porni sistemul Jenkins din moment ce aplicatia asculta pe portul 8080.
Pentru prima folosire este cerut Administrator password.Pentru aceasta va trebui sa accesam un fisier secret care se gaseste accesand calea urmatoare: 
$sudo cat /var/lib/Jenkins/secrets/initialAdminPassword – ne va da in consola CLI parola de tip hash pe care o introducem in Jenkins. De aici vom configura contul de Jenkins care se ocupa de acest repository si de aici putem crea teste pentru script-uri – Freestyle,Pipeline Install suggested Plugins Create account -> user = admin ; password = admin -> Save and Continue -> Manage Jenkins -> Install Plugins -> Available Plugins -> Search Blue Ocean -> Install

Instalare docker:
1.sudo apt-get update
2.sudo apt-get install ca-certificates curl gnupg lsb-release
3.sudo mkdir -p /etc/apy/keyrings
4.curl -fsSL | sudo gpg –dearmor -o /etc/apy/keyrings/docker.gpg 
5.echo “deb [arch=$(dpkg –print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] $(lsb_release -cs) stable”| sudo tee /etc/apt/sources.list.d/docker.list > /dev/null 
6.sudo apt-get update 
7.sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin docker-compose Pentru a face acest lucru este necesar un Dockerfile, o imagine cu numele – 444D_flori, un fisier pentru a porni serviciul docker – dockerstart.sh
Status docker:
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/84671601/6a08fd5c-62aa-470a-888f-b90009bb2adf)

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/84671601/aa8bf557-1190-4d10-839a-788a0b05d1d6)

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/84671601/d21b3202-3b62-48c4-98f7-e9e4f22ea625)


Pentru a crea imaginea, folosim comanda:
$sudo docker build -t 444d_flori:v01 .

Pentru a rula containerul, folosim comanda:
$sudo docker run --name 444D_flori -p 8020:5001 444d_flori:v01 8020 – portul de pe masina locala unde va raspunde serverul din docker 5001 – portul din interiorul containerului 444d_flori – numele containerului 444D_flori – numele repository-ului :v01 – versiunea pentru container


Comenzile folosite pentru realizarea acestui proiect sunt:

  1  sudo apt update
    2  sudo apt install git
    3  suudo apt update
    4  sudo apt update
    5  sudo apt install git
    6  sudo apt install gedit\
    7  sudo apt install gedit
    8  sudo apt install vim
    9  sudo apt install python4
   10  sudo apt install python3
   11  sudo apt install pytest
   12  sudo apt install pip
   13  pip install pytest
   14  sudo apt install pytest
   15  sudo apt install jenkins
   16  sudo apt install docker
   17  sudo apt install jenkins\
   18  sudo apt install jenkins
   19  cd desktop
   20  cd Desktop
   21  ls -l
   22  ls -a
   23  ls -la
   24  sudo apt install git
   25  cd
   26  ls -la
   27  sudo apt install git
   28  sudo apt autremove git
   29  sudo apt autoremove git
   30  cd Desttop
   31  cd Desktop
   32  mkdier git
   33  mkdir git
   34  cd git
   35  sudo apt install git
   36  sudo apt install gedit
   37  sudo apt-get update
   38  sudo apt install build-essential dkms linux-headers-$(uname -r)
   39  git clone https://github.com/andrei162/curs_vcgj_444D_flori.git
   40  sudo apt install python 3
   41  sudo apt install python3
   42  python3 444D_flory.py
   43  ls -la
   44  cd curs_vcgj_444D_flori/
   45  ls
   46  cd app
   47  ls
   48  python3 444D_flory.py
   49  python3 444D_flori.py
   50  cd ..
   51  sudo apt install flask
   52  sudo apt install python3-flask
   53  sudo apt install python3-pip
   54  pip instal pytest
   55  pip install pytest
   56  python3 -m pytest -v
   57  python3 444D_flori.py
   58  ls
   59  cd curs_vcgj_444D_flori/
   60  cd app/
   61  cd curs_vcgj_444D_flori/
   62  python3 444D_flori.py
   63  python3 -m pytest -v
   64  git config --global user.email "draguletevalerian@gmail.com"
   65  git config --global user.name "validragulete"
   66  git config --global credidential.helper store
   67  cd ..
   68  touch Jenkinsfile
   69  gedit Jenkinsfile 
   70  cd app
   71  touch activeaza_venv
   72  gedit activeaza_venv 
   73  tail activeaza_venv 
   74  touch activeaza_venv_jenkins
   75  gedit activeaza_venv_jenkins 
   76  touch ruleaza_aplicatia
   77  gedit ruleaza_aplicatia 
   78  git branch
   79  cd ..
   80  cd curs_vcgj_444D_flori/
   81  git branch devel/validragulete_flori
   82  git branch
   83  git checkout 
   84  git checkout devel/validragulete_flori 
   85  git branch 
   86  git sta
   87  git status 
   88  git add .
   89  git status
   90  git commit -n "tare"
   91  git commit -m "tare"
   92  git branch 
   93  git sta
   94  git status 
   95  git config --global credential.helper store
   96  git push
   97  git push --set-upstream origin devel/validragulete_flori 
   98  git psuh
   99  git push
  100  git branch
  101  history 
  102  cd Desktop/
  103  touch token
  104  gedit token 
  105  cd c
  106  cd git/
  107  cd curs_vcgj_444D_flori/
  108  ls -l
  109  tail -n 10 Jenkinsfile 
  110  java -ver
  111  sudo apt install java
  112  cd Desktop/
  113  ls
  114  touch parolaJenkins
  115  gedit parolaJenkins 
  116  tail parolaJenkins 
  117  sudo apt install openjdk-11-jdk
  118  history 
  119  history 113
  120  sudo apt install curl
  121  curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee   /usr/share/keyrings/jenkins-keyring.asc > /dev/null
  122  echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]   https://pkg.jenkins.io/debian-stable binary/ | sudo tee   /etc/apt/sources.list.d/jenkins.list > /dev/null
  123  curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee   /usr/share/keyrings/jenkins-keyring.asc > /dev/null
  124  echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]   https://pkg.jenkins.io/debian-stable binary/ | sudo tee   /etc/apt/sources.list.d/jenkins.list > /dev/null
  125  sudo apt-get update
  126  sudo apt-get install jenkins
  127  sudo systemctl status jenins
  128  sudo systemctl status jenkins
  129  sudo cat /var/lib/jenkins/secrets/initialAdminPassword
  130  git hist
  131  host
  132  history 
  133  cd app
  134  source activeaza_venv
  135  source activeaza_venv_jenkins 
  136  git status 
  137  source ruleaza_aplicatia 
  138  gedit 444D_flori.py 
  139  sudo apt install python3.10-venv
  140  sudo apt install python3-venv
  141  git push
  142  git add .
  143  git status
  144  git push
  145  history
  146  git branch 
  147  cd Desktop/git/curs_vcgj_444D_flori/
  148  git branch 
  149  sudo apt-get update
  150  sudo apt-get intsall ca-certificates curl
  151  sudo apt-get install ca-certificates curl
  152  sudo apt-get install ca-certificates curl gnupg lsb-release
  153  cd
  154  sudo apt-get install ca-certificates curl gnupg lsb-release
  155  sudo mkdir -p /etc/apt/keyrings/
  156  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
  157  echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  158  sudo apt-get update
  159  sudo chmod 777 /etc/apt/keyrings/docker.gpg
  160  sudo apt-get update 
  161  sudo chmod 777 /etc/apt/keyrings/docker.gpg
  162  sudo apt-get update 
  163  sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin docker-compose –y
  164  sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin docker-compose
  165  sudo apt-get update 
  166  sudo apt-get install ca-certificates curl gnupg lsb-release
  167  sudo mkdir -p /etc/apt/keyrings
  168  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
  169  echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  170  sudo apt-get update
  171  sudo chmod a+r /etc/apt/keyrings/docker.gpg
  172  sudo apt-get update
  173  sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin docker-compose
  174  cd Desktop/git/curs_vcgj_444D_flori/
  175  touch Dockerfile
  176  gedit Dockerfile 
  177  ls
  178  cd app
  179  touch quickrequirements
  180  gedit quickrequirements 
  181  rm -r quickrequirements 
  182  ls
  183  touch dockerstart.sh
  184  gedit dockerstart.sh 
  185  touch quickrequirements.txt
  186  gedit quickrequirements.txt 
  187  ls -la
  188  cd ..
  189  sudo docker build -t 444d_flori:v01 .
  190  cd app
  191  source activeaza_venv
  192  cd ..
  193  sudo docker images
  194  sudo docker run
  195  sudo docker run --name 444d_flori -p 8020:6020 444d_flori:v01 .
  196  deactivate
  197  sudo docker images
  198  sudo docker rmi 8ec571a91884
  199  activate
  200  cd app
  201  source activeaza_venv
  202  cd ..
  203  sudo docker rmi 8ec571a91884
  204  sudo docker rml 8ec571a91884
  205  sudo docker ps -a
  206  sudo docker rmi 88cb7a66504a
  207  sudo docker images
  208  sudo docker rmi 8ec571a91884
  209  cd
  210  deactivate 
  211  sudo nano /etc/default/jenkins
  212  sudo systemctl restart jenkins+
  213  sudo systemctl restart jenkins
  214  sudo docker iamges
  215  sudo docker images
  216  sudo docker rmi sudo systemctl restart jenkins
  217  sudo docker build -t 444d_flori:v01 .
  218  sudo docker rmi 8ec571a91884
  219  sudo docker rmi -r 8ec571a91884
  220  docker rmi --help
  221  sudo docker rmi -f 8ec571a91884
  222  git status
  223  git add .
  224  git commit 
  225  git commit "am facut docker-ul"
  226  history 
  227  git commit -m "am facut docker-ul"
  228  git push
  229  ls
  230  cd lib
  231  mkdir lib
  232  cd lib
  233  touch biblioteca_flori.py
  234  gedit biblioteca_flori.py 
  235  cd ..
  236  cd app
  237  gedit 444D_flori.py 
  238  cd ..
  239  cd lib
  240  gedit biblioteca_flori.py 
  241  cd ..
  242  git add .
  243  git commit -m "sper ca e gata"
  244  git push
  245  sudo docker build -t 444d_flori:v01 .
  246  sudo docker run
  247  sudo docker run --name 444d_flori -p 8020:5020 444d_flori:v01 .
  248  docker images
  249  sudo docker run --name 444d_flori -p 8020:5020 444d_flori:v01 .
  250  docker ps -a
  251  sudo docker images
  252  sudo docker run --name 444d_flori -p 8020:5020 444d_flori:v01 .
  253  sudo docker run
  254  sudo docker run --help
  255  sudo docker run --name 444d_flori_vali -p 8020:5020 444d_flori:v01 .
  256  cd app
  257  ls
  258  chmod 777 dockerstart.sh 
  259  cd ..
  260  sudo docker run --name 444d_flori_vali -p 8020:5020 444d_flori:v01 .
  261  sudo docker images
  262  sudo docker run --name 444d_flori
  263  sudo docker run --name 444d_flori_vali -p 8020:5020 444d_flori:v01 .
  264  sudo docker run --name 444d_flori -p 8020:5020 444d_flori:v01 .
  265  sudo docker rmi 88cb7a66504a5fbac2c0a2fbde5025168b128b96e7e44fc5c9b51660f013876b
  266  sudo docker run --name 444d_flori -p 8020:5020 444d_flori:v01 .
  267  docker run --help
  268  sudo docker run --name 444d_flori -p 8020:5020 444d_flori:v01 .
  269  sudo docker rmi 444d_flori
  270  sudo systemctl restart docker
  271  sudo docker run --name 444d_flori -p 8020:5020 444d_flori:v01 .
  272  sudo docker images
  273  sudo docker rmi 52ab21f989c6
  274  sudo docker rmi -f 52ab21f989c6
  275  sudo systemctl restart docker
  276  history 
  277  sudo docker build -t 444d_flori:v01 .
  278  sudo docker run --name 444d_flori -p 8020:5020 444d_flori:v01 .
  279  git status
  280  docker start
  281  docker start 88cb7a66504a5fbac2c0a2fbde5025168b128b96e7e44fc5c9b51660f013876b
  282  sudo docker run --name 444d_flori -p 8020:5020 444d_flori:v01 .
  283  sudo docker start -a 444d_flori
  284  sudo docker images
  285  sudo docker rmi -f 8361c0932ae4
  286  sudo docker images
  287  cd app
  288  sudo chmod 777 dockerstart.sh 
  289  cd ..
  290  cd app
  291  gedit dockerstart.sh 
  292  git add .
  293  git commit -m "sper sa meargav2"
  294  git push
  295  history 
  296  sudo systemctl restart docker
  297  cd ..
  298  sudo docker build -t 444d_flori:v01 .
  299  sudo docker run --name 444d_flori -p 8020:5020 444d_flori:v01 .
  300  sudo docker run --name 444d_florii -p 8020:5020 444d_flori:v01 .
  301  ls
  302  cd app
  303  ls
  304  cd ..
  305  sudo docker ps -a
  306  sudo docker rmi -f aec5abbc6596
  307  sudo docker rm aec5abbc6596
  308  sudo docker ps -a
  309  sudo docker rm 52ab21f989c6
  310  sudo docker rm d969ffabc2c2
  311  sudo docker ps -a
  312  sudo docker rm 88cb7a66504a
  313  sudo docker images
  314  history
  315  sudo docker run --name 444d_flori -p 8020:5020 444d_flori:v01 .
  316  sudo docker start --name 444d_flori
  317  sudo docker start
  318  sudo docker start --help
  319  sudo docker ps -a
  320  sudo docker start 784f9392b40a
  321  sudo docker ps -a
  322  sudo docker start 784f9392b40a
  323  git status
  324  git add .
  325  git commit -m "am modificat biblioteca"
  326  git push
  327  history
  328  sudo docker ps -a
  329  sudo docker rm 784f9392b40a
  330  sudo docker rm -f 784f9392b40a
  331  sudo docker ps -a
  332  sudo docker run --name 444d_flori -p 8020:5020 444d_flori:v01 .
  333  sudo docker ps -a
  334  sudo docker rm -f 9bb845fdf0b1
  335  sudo docker ps -a
  336  history 
  337  sudo docker run --name 444d_flori -p 8020:5020 444d_flori:v01 .
  338  docker ps -a
  339  sudo docker ps -a
  340  sudo docker rm -f 4e2e7d6e38d9
  341  history 
  342  sudo docker run --name 444d_flori -p 8020:5020 444d_flori:v01 .
  343  sudo docker ps -a
  344  sudo docker rm -f 868c83c6a4ce
  345  sudo docker ps -a
  346  sudo docker rm -f c54abab584c1
  347  sudo docker ps -a
  348  sudo docker run --name 444d_flori -p 8020:5020 444d_flori:v01 .
  349  ps -a
  350  sudo docker ps -a
  351  sudo docker rm -f b584fb7697cc
  352  git stauts
  353  git status
  354  git add .
  355  git commit -m "test"
  356  git push
  357  sudo docker run --name 444d_flori -p 8020:5020 444d_flori:v01 .
  358  hist
  359  history 
  360  sudo docker ps -a
  361  sudo docker rm -f e42f31a12916
  362  sudo docker iamges
  363  sudo docker image
  364  sudo docker images
  365  sudo docker rmi 8361c0932ae4
  366  history
  367  sudo docker build -t 444d_flori:v01 .
  368  sudo docker run --name 444d_flori -p 8020:5020 444d_flori:v01 .
  369  history 
  370  sudo docker ps -a
  371  1549a5d95915
  372  sudo docker rm -f 1549a5d95915
  373  sudo docker images
  374  sudo docker rmi 04bb9d920b3f
  375  git add .
  376  git commit -m "modificare finala(sper)"
  377  git push
  378  history 
  379  sudo docker build -t 444d_flori:v01 .
  380  sudo docker run --name 444d_flori -p 8020:5020 444d_flori:v01 .
