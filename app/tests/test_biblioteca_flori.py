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
        
def test_culoare_narcisa():
    cul = bflori.culoare_narcisa()
    if cul == "alb" : 
        assert True
    else: 
        assert False
        

def test_anotimp_narcisa():
    cul = bflori.anotimp_narcisa()
    if cul == "primavara" :
        assert True
    else: 
        assert False

def test_clasificare_narcisa():
    cul = bflori.clasificare_narcisa()
    if cul == "frumoasa" :
        assert True
    else: 
        assert False
