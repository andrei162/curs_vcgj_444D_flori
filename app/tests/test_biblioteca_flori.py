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
     
def test_culoare_trandafir():
    cul = bflori.culoare_trandafir()
    if cul == "rosu" : 
        assert True
    else: 
        assert False
        

def test_anotimp_trandafir():
    cul = bflori.anotimp_trandafir()
    if cul == "toamna" :
        assert True
    else: 
        assert False

def test_clasificare_trandafir():
    cul = bflori.clasificare_trandafir()
    if cul == "aromat" :
        assert True
    else: 
        assert False
