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
        
def test_culoare_bonsai():
    cul = bflori.culoare_bonsai()
    if cul == "roz" : 
        assert True
    else: 
        assert False
        

def test_anotimp_bonsai():
    cul = bflori.anotimp_bonsai()
    if cul == "primavara" :
        assert True
    else: 
        assert False

def test_clasificare_bonsai():
    cul = bflori.clasificare_bonsai()
    if cul == "infrumusetare" :
        assert True
    else: 
        assert False
