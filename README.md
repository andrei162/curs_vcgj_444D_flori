# curs_vcgj_444D_flori
Floarea aleasa: Zambila
Mihai Carmen-Andreea 444D

  Am instalat toate programele de care voi avea nevoie in realizarea proiectului (Jenkins, git, Docker) in timpul laboratoarelor. Am instalat si dependinetele care lipseau utilizand comenzile urmatoare:
    sudo apt install python3-pip
    pip install pytest
    sudo apt install gedit
    pip install flask
    sudo apt install python3-venv
  Am clonat repository-ul de pe github:
   git clone https://github.com/andrei162/curs_vcgj_444D_flori.git
  Am creat pe desktop :
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/133675024/978a12b2-755f-450d-8c7a-49f7e0f3d9e9)
  Putem vizualiza si fisierele din interiorul lui:
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/133675024/4139189e-7770-4cf2-8739-12bdf71ca4c4)

 Am creat un branch nou numit devel/amihai24_flori cu comanda git branch si m-am mutat pe noul branch cu comanda git checkout.

Fisierul 444D_flori contine toate metodele de GET si POST din aplicatia noastra. Aici se face redirectionarea catre paginile specifice fiecarei functii si cereri implementate in proiect. Voi edita fisierul cu gedit si voi adauga functionalitatile corespunzatoare florii alese. Floarea aleasa este zambila, de culoare mov si din anotimpul primavara,din categoria Hyacinthus orientalis.
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/133675024/b4c8a776-d654-473e-9a6b-1fe98d92f9de)

In folderul tests exista si un fisier numit test_biblioteca_flori.py in care sunt implementate teste pentru verificarea functionarii corecte a aplicatiei. In fiecare test am setat parametrul care ar trebui sa fie returnat de functiile definite in biblioteca_flori.py si am verificat daca acesta corespunde cu ceaa ce returneaza functiile de fapt:
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/133675024/88d2fb7c-d557-4b9f-a4fe-b521191e0ed8)
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/133675024/93f3c680-8982-40f0-a659-0151556b439e)

Pentru a rula testele am folosit comanda:

python3 -m pytest ./tests -v
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/133675024/a7526f93-85b1-4c27-b6c1-877fee83abb5)
Voi porni aplicatia utilizand comanda:
python3 444D_flori.py

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/133675024/f3041e9d-f72f-44a4-a633-ba20b8378a4c)
Voi verifica daca toate paginile exista si sunt functionale:

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/133675024/c3a7463d-32e7-4520-b809-bd51228f73fd)
zambila/culoare
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/133675024/b74a050d-391e-4612-81a8-df48c1d5d940)
zambila/anotimp
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/133675024/ad09bc4d-1796-4396-ac20-c3b1f45b7818)
zambila/clasificare
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/133675024/7de11ae6-22d7-4dc3-9d7e-1a8a00af5cbc)
Pentru docker:
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/133675024/53353af6-1387-4ebb-99f3-86194a9f1686)
Open Blue Ocean, Jenkins:
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/133675024/28dee119-ca7d-41aa-8421-8083ae772305)

Pentru a urca modificarile facute in fisiere pe github, am rulat comenzile:
    git add .
    git commit -m
    git push
 ![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/133675024/8d9459ed-a2ec-4fd8-a423-bc5ecac79998)














