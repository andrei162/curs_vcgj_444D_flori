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
    
@app.route("/ghiocel/", methods=['GET'])
def get_ghiocel():
    ret = "<h1>ghiocel<h1>"
    ret += "Culoare: "
    ret += lib.biblioteca_flori.culoare_ghiocel()
    ret += "<br>"
    
    ret += "Anotimp: "
    ret += lib.biblioteca_flori.anotimp_ghiocel()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += lib.biblioteca_flori.clasificare_ghiocel()
    ret += "<br>"
    
    return ret
    
@app.route("/ghiocel/culoare", methods=['GET'])
def ia_culoare_ghiocel():
    ret = ""
    ret += lib.biblioteca_flori.culoare_ghiocel()
    
    return ret
    
@app.route("/ghiocel/anotimp", methods=['GET'])
def ia_anotimp_ghiocel():
    ret = ""
    ret += lib.biblioteca_flori.anotimp_ghiocel()
    
    return ret
    
@app.route("/ghiocel/clasificare", methods=['GET'])
def ia_clasificare_ghiocel():
    ret = ""
    ret += lib.biblioteca_flori.clasificare_ghiocel()
    
    return ret
    
@app.route("/hibiscus/", methods=['GET'])
def get_hibiscus():
    ret = "<h1>Hibiscus<h1>"
    ret += "Culoare: "
    ret += lib.biblioteca_flori.culoare_hibiscus()
    ret += "<br>"
    
    ret += "Anotimp: "
    ret += lib.biblioteca_flori.anotimp_hibiscus()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += lib.biblioteca_flori.clasificare_hibiscus()
    ret += "<br>"
    
    return ret
    
@app.route("/hibiscus/culoare", methods=['GET'])
def ia_culoare_hibiscus():
    ret = ""
    ret += lib.biblioteca_flori.culoare_hibiscus()
    
    return ret
    
@app.route("/hibiscus/anotimp", methods=['GET'])
def ia_anotimp_hibiscus():
    ret = ""
    ret += lib.biblioteca_flori.anotimp_hibiscus()
    
    return ret
    
@app.route("/hibiscus/clasificare", methods=['GET'])
def ia_clasificare_hibiscus():
    ret = ""
    ret += lib.biblioteca_flori.clasificare_hibiscus()
    
    return ret
    
    
app.run(host = "127.0.0.1", port = 5001)
