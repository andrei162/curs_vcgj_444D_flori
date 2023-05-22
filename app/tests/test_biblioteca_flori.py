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
        
def test_culoare_margareta():
    cul = bflori.culoare_margareta()
    if cul == "alb" : 
        assert True
    else: 
        assert False
        
def test_anotimp_margareta():
    cul = bflori.anotimp_margareta()
    if cul == "primavara" :
        assert True
    else: 
        assert False

def test_clasificare_margareta():
    cul = bflori.clasificare_margareta()
    if cul == "Asteraceae" :
        assert True
    else: 
        assert False   
