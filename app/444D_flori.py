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
    
@app.route("/Dalie/", methods=['GET'])
def get_Dalie():
    ret = "<h1>Dalie<h1>"
    ret += "Culoare: "
    ret += lib.biblioteca_flori.culoare_Dalie()
    ret += "<br>"
    
    ret += "Anotimp: "
    ret += lib.biblioteca_flori.anotimp_Dalie()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += lib.biblioteca_flori.clasificare_Dalie()
    ret += "<br>"
    
    return ret
    
@app.route("/Dalie/culoare", methods=['GET'])
def ia_culoare_Dalie():
    ret = ""
    ret += lib.biblioteca_flori.culoare_Dalie()
    
    return ret
    
@app.route("/Dalie/anotimp", methods=['GET'])
def ia_anotimp_Dalie():
    ret = ""
    ret += lib.biblioteca_flori.anotimp_Dalie()
    
    return ret
    
@app.route("/Dalie/clasificare", methods=['GET'])
def ia_clasificare_Dalie():
    ret = ""
    ret += lib.biblioteca_flori.clasificare_Dalie()
    
    return ret
    
app.run(host = "127.0.0.1", port = 5001)
