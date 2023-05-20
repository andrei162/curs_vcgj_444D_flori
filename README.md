# curs_vcgj_444D_flori
Inainte sa clonez repozitorul lui andrei local, am instalat gedit pentru a putea edita mai usor fisiere, flask, pytest si alte softuri necesare pe care nu le aveam de la laboratoare.
In directorul git_proiect (destinat aplicatiei) aveam deja repozitorul clonat local de mai de mult si nu a fost nevoie sa o fac din nou.

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/92923136/26e5a823-da90-499d-9926-646deea9f9f3)

Pentru inceput am editat fisierul biblioteca_flori.py din /app/lib adaugand floarea de colt in biblioteca.

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/92923136/ebdc9bb1-3067-447b-a006-07abc1a073c5)

Am adaugat in directorul de teste din /app in fisierul test_biblioteca_flori.py floarea de colt.

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/92923136/36a4a79a-caa0-4b12-a7f3-98688ebab9c3)

Dupa ce adaugam si rutele in /app 444D_flori.py o sa putem testa local aplicatia.

############################
############################

@app.route("/floaredecolt/", methods=['GET'])
def get_floaredecolt():
    ret = "<h1>Floare de Colt<h1>"
    ret += "Culoare: "
    ret += lib.biblioteca_flori.culoare_floaredecolt()
    ret += "<br>"
    
    ret += "Anotimp: "
    ret += lib.biblioteca_flori.anotimp_floaredecolt()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += lib.biblioteca_flori.clasificare_floaredecolt()
    ret += "<br>"
    
    return ret
    
@app.route("/floaredecolt/culoare", methods=['GET'])
def ia_culoare_floaredecolt():
    ret = ""
    ret += lib.biblioteca_flori.culoare_floaredecolt()
    
    return ret
    
@app.route("/floaredecolt/anotimp", methods=['GET'])
def ia_anotimp_floaredecolt():
    ret = ""
    ret += lib.biblioteca_flori.anotimp_floaredecolt()
    
    return ret
    
@app.route("/floaredecolt/clasificare", methods=['GET'])
def ia_clasificare_floaredecolt():
    ret = ""
    ret += lib.biblioteca_flori.clasificare_floaredecolt()
    
    return ret

############################
############################
  
Aplicatia Flask ruleaza
    
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/92923136/ed57581e-4f7e-4f3b-86ec-77c9f72380f7)
    
Folosim pytest pentru a verifica
    
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/92923136/0065b7f9-e5a4-4a33-8fc8-122bd5a5c239)

Mai departe creez in /app fisierele activeaza_venv, activeaza_venv_jenkins si ruleaza_aplicatia si fisierul pipeline Jenkinsfile pentru a putea testa aplicatia online cu Jenkins.
    
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/92923136/8c10d9ba-cce2-459b-b260-03ea61cd1891)

Creez un branch de developer local pentru a nu modifica aplicatia principala cand voi da push pe git. Aceasta va fi modificata ulterior cu aprobarea coordonatorilor.

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/92923136/55fed55a-393d-4a08-bfc7-1ed48bb7786f)

Se observa multe modificari care nu sunt de fapt adaugate pe niciun branch si sunt facute doar local.
Schimbam branchul pe cel creat mai devreme.

![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/92923136/0d7a8178-a71f-453a-8ace-09762c368e94)

Dupa asta, folosim git add pentru adaugarea modificarilor pe branch si ulterior git commit.
    
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/92923136/8a6ca4d4-7025-49f8-a14b-a2ac768ecfc2)
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/92923136/0db1d12f-7e99-4bce-b24d-5855d9455580)

In final pentru a actualiza repozitorul din cloud cu modificarile aduse la aplicatie local, folosim comanda git push. Primeam o eroare in care mi se sugera utilizarea optiunii --set-upstream
    
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/92923136/b80e2a0c-9722-4e1d-b9fb-9c1773e77f15)

Acum aplicatia se afla in cloud si mai departe putem folosi Jenkins ca sa verificam functionalitatea aplicatiei pe server.
Dupa ce instalam Jenkins si toate cele necesare pentru a utiliza lui acessam localhost:8080 . Ne logam si cream un nou job pipeline.
    
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/92923136/5d7e28bd-4ca0-46e1-9b21-f13cd340090d)
    
Trebuie sa specificam ca codul sursa al aplicatiei pe care vrem sa o testam se afla in cloudul git. Luam URL ul repoului proiectului si il copiem in Jenkins. De asemenea specificam branchul pe care dorim sa il folosim */devel/paulicaETTI_flori
    
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/92923136/c9c67d02-ebad-4c1c-8b3f-c7551a5c8367)  
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/92923136/3da0b694-ea4e-480c-b542-4381d78ceb82)
    
Dupa build aplicatiei de pe branchul devel are succes. Se poate folosi si Blueocean pentru mai multe detalii ale buildului de pipeline.
    
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/92923136/1ca8e427-b3e8-4bb7-82f9-1c6320c0476d)
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/92923136/0f117d77-5e38-46de-98e3-7c9a66451191)

Acum ca aplicatia este pregatita de a rula online pe server ne ocupam de containerizarea ei cu Docker.
    





    




    
 
