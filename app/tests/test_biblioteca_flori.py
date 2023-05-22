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
       
def test_culoare_Dalie():
    cul = bflori.culoare_Dalie()
    if cul == "roz" : 
        assert True
    else: 
        assert False
        

def test_anotimp_Dalie():
    cul = bflori.anotimp_Dalie()
    if cul == "vara" :
        assert True
    else: 
        assert False

def test_clasificare_Dalie():
    cul = bflori.clasificare_Dalie()
    if cul == "safe" :
        assert True
    else: 
        assert False
