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
        
def test_culoare_lalea():
    cul = bflori.culoare_lalea()
    if cul == "Roz" : 
        assert True
    else: 
        assert False
        
def test_anotimp_lalea():
    cul = bflori.anotimp_lalea()
    if cul == "Primavara" :
        assert True
    else: 
        assert False

def test_clasificare_lalea():
    cul = bflori.clasificare_lalea()
    if cul == "Liliaceae" :
        assert True
    else: 
        assert False        
