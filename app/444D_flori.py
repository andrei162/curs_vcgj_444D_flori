from flask import Flask

import lib.biblioteca_flori

app = Flask(__name__)

print('444D_flori')

@app.route("/" , methods=['GET'])
def index():
    ret = "<h1></h1>Informatii despre flori 444D</h1>"
    return ret

@app.route("/crin/", methods=['GET'])
def get_crin():
    ret = "<h1>Crin<h1>"
    ret += "Culoare: "
    ret += lib.biblioteca_flori.culoare_crin()
    ret += "<br>"
    
    ret += "Anotimp: "
    ret += lib.biblioteca_flori.anotimp_crin()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += lib.biblioteca_flori.clasificare_crin()
    ret += "<br>"
    
    return ret
    
@app.route("/crin/culoare", methods=['GET'])
def ia_culoare_crin():
    ret = ""
    ret += lib.biblioteca_flori.culoare_crin()
    
    return ret
    
@app.route("/crin/anotimp", methods=['GET'])
def ia_anotimp_crin():
    ret = ""
    ret += lib.biblioteca_flori.anotimp_crin()
    
    return ret
    
@app.route("/crin/clasificare", methods=['GET'])
def ia_clasificare_crin():
    ret = ""
    ret += lib.biblioteca_flori.clasificare_crin()
    
    return ret
    
@app.route("/liliac/", methods=['GET'])
def get_liliac():
    ret = "<h1>Liliac<h1>"
    ret += "Culoare: "
    ret += lib.biblioteca_flori.culoare_liliac()
    ret += "<br>"
    
    ret += "Anotimp: "
    ret += lib.biblioteca_flori.anotimp_liliac()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += lib.biblioteca_flori.clasificare_liliac()
    ret += "<br>"
    
    return ret
    
@app.route("/liliac/culoare", methods=['GET'])
def ia_culoare_liliac():
    ret = ""
    ret += lib.biblioteca_flori.culoare_liliac()
    
    return ret
    
@app.route("/liliac/anotimp", methods=['GET'])
def ia_anotimp_liliac():
    ret = ""
    ret += lib.biblioteca_flori.anotimp_liliac()
    
    return ret
    
@app.route("/liliac/clasificare", methods=['GET'])
def ia_clasificare_liliac():
    ret = ""
    ret += lib.biblioteca_flori.clasificare_liliac()
    
    return ret
    
    
app.run(host = "127.0.0.1", port = 5001)


