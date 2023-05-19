from flask import Flask

import lib.biblioteca_flori

app = Flask(__name__)

print('444D_flori')

@app.route("/" , methods=['GET'])
def index():
    ret = "<h1></h1>Informatii despre flori 444D</h1>"
    return ret

@app.route("/bonsai/", methods=['GET'])
def get_bonsai():
    ret = "<h1>bonsai<h1>"
    ret += "Culoare: "
    ret += lib.biblioteca_flori.culoare_bonsai()
    ret += "<br>"
    
    ret += "Anotimp: "
    ret += lib.biblioteca_flori.anotimp_bonsai()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += lib.biblioteca_flori.clasificare_bonsai()
    ret += "<br>"
    
    return ret
    
@app.route("/bonsai/culoare", methods=['GET'])
def ia_culoare_bonsai():
    ret = ""
    ret += lib.biblioteca_flori.culoare_bonsai()
    
    return ret
    
@app.route("/bonsai/anotimp", methods=['GET'])
def ia_anotimp_bonsai():
    ret = ""
    ret += lib.biblioteca_flori.anotimp_bonsai()
    
    return ret
    
@app.route("/bonsai/clasificare", methods=['GET'])
def ia_clasificare_bonsai():
    ret = ""
    ret += lib.biblioteca_flori.clasificare_bonsai()
    
    return ret
    
    
app.run(host = "127.0.0.1", port = 5001)
