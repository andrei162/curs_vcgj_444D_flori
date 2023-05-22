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
    if cul == "parfumat" :
        assert True
    else: 
        assert False
        
def test_culoare_hortensie():
    cul = bflori.culoare_hortensie()
    if cul == "alb" : 
        assert True
    else: 
        assert False
        

def test_anotimp_hortensie():
    cul = bflori.anotimp_hortensie()
    if cul == "vara" :
        assert True
    else: 
        assert False

def test_clasificare_hortensie():
    cul = bflori.clasificare_hortensie()
    if cul == "parfumat" :
        assert True
    else: 
        assert False
