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
        
def test_culoare_camelie():
    cul = bflori.culoare_camelie()
    if cul == "roz" : 
        assert True
    else: 
        assert False
        

def test_anotimp_camelie():
    cul = bflori.anotimp_camelie()
    if cul == "primavara" :
        assert True
    else: 
        assert False

def test_clasificare_camelie():
    cul = bflori.clasificare_camelie()
    if cul == "Camellia Japonica" :
        assert True
    else: 
        assert False
