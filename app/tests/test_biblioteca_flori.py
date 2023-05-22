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
        
def test_culoare_bujor():
    cul = bflori.culoare_bujor()
    if cul == "rosie" : 
        assert True
    else: 
        assert False
        

def test_anotimp_bujor():
    cul = bflori.anotimp_bujor()
    if cul == "primavara" :
        assert True
    else: 
        assert False

def test_clasificare_bujor():
    cul = bflori.clasificare_bujor()
    if cul == "parfumat" :
        assert True
    else: 
        assert False
