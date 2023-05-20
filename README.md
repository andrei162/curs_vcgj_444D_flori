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
  
 
![image](https://github.com/andrei162/curs_vcgj_444D_flori/assets/92923136/ed57581e-4f7e-4f3b-86ec-77c9f72380f7)
