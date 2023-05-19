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
        
def test_culoare_floaredecolt():
    cul = bflori.culoare_floaredecolt()
    if cul == "alb" : 
        assert True
    else: 
        assert False
        

def test_anotimp_floaredecolt():
    cul = bflori.anotimp_floaredecolt()
    if cul == "vara" :
        assert True
    else: 
        assert False

def test_clasificare_floaredecolt():
    cul = bflori.clasificare_floaredecolt()
    if cul == "frumusete" :
        assert True
    else: 
        assert False
