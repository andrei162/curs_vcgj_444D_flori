import lib.biblioteca_flori as bflori

def test_culoare_crin():
    cul = bflori.culoare_crin()
    if cul == "alb" : 
        assert True
    else: 
        assert False
        

def test_anotimp_crin():
    cul = bflori.anotimp_crin()
    if cul == "vara" :
        assert True
    else: 
        assert False

def test_clasificare_crin():
    cul = bflori.clasificare_crin()
    if cul == "toxic" :
        assert True
    else: 
        assert False
        
def test_culoare_lavanda():
    cul = bflori.culoare_lavanda()
    if cul == "violet" : 
        assert True
    else: 
        assert False
        

def test_anotimp_lavanda():
    cul = bflori.anotimp_lavanda()
    if cul == "vara" :
        assert True
    else: 
        assert False

def test_clasificare_lavanda():
    cul = bflori.clasificare_lavanda()
    if cul == "terapeutic" :
        assert True
    else: 
        assert False
