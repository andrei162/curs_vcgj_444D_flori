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
        
def test_culoare_floarea_pastelui():
    cul = bflori.culoare_floarea_pastelui()
    if cul == "oranj" : 
        assert True
    else: 
        assert False
        

def test_anotimp_floarea_pastelui():
    cul = bflori.anotimp_floarea_pastelui()
    if cul == "primavara" :
        assert True
    else: 
        assert False

def test_clasificare_floarea_pastelui():
    cul = bflori.clasificare_floarea_pastelui()
    if cul == "decorativa" :
        assert True
    else: 
        assert False
