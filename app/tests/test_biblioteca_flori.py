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
        
def test_culoare_zambila():
    cul = bflori.culoare_zambila()
    if cul == "mov" : 
        assert True
    else: 
        assert False
        

def test_anotimp_zambila():
    cul = bflori.anotimp_zambila()
    if cul == "primavara" :
        assert True
    else: 
        assert False

def test_clasificare_zambila():
    cul = bflori.clasificare_zambila()
    if cul == "parfumat" :
        assert True
    else: 
        assert False
