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
    
@app.route("/lalea/", methods=['GET'])
def get_lalea():
	ret = "<h1>Lalea<h1>"
	ret += "Culoare: "
	ret += lib.biblioteca_flori.culoare_lalea()
	ret += "<br>"
	
	ret += "Anotimp: "
	ret += lib.biblioteca_flori.anotimp_lalea()
	ret += "<br>"
    
	ret += "Clasificare: "
	ret += lib.biblioteca_flori.clasificare_lalea()
	ret += "<br>"
	
	return ret
    
@app.route("/lalea/culoare", methods=['GET'])
def ia_culoare_lalea():
	ret = ""
	ret += lib.biblioteca_flori.culoare_lalea()
    
	return ret
    
@app.route("/lalea/anotimp", methods=['GET'])
def ia_anotimp_lalea():
	ret = ""
	ret += lib.biblioteca_flori.anotimp_lalea()
    
	return ret
    
@app.route("/lalea/clasificare", methods=['GET'])
def ia_clasificare_lalea():
	ret = ""
	ret += lib.biblioteca_flori.clasificare_lalea()
    
	return ret    
    
    
    
#app.run(host = "127.0.0.1", port = 5001)
