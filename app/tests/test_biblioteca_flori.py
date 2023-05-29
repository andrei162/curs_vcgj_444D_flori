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
        
        
def test_culoare_ghiocel():
    cul = bflori.culoare_ghiocel()
    if cul == "alb" : 
        assert True
    else: 
        assert False
        

def test_anotimp_ghiocel():
    cul = bflori.anotimp_ghiocel()
    if cul == "primavara" :
        assert True
    else: 
        assert False

def test_clasificare_ghiocel():
    cul = bflori.clasificare_ghiocel()
    if cul == "parfumat" :
        assert True
    else: 
        assert False   
        
        
def test_culoare_hibiscus():
    cul = bflori.culoare_hibiscus()
    if cul == "roz" : 
        assert True
    else: 
        assert False
        

def test_anotimp_hibiscus():
    cul = bflori.anotimp_hibiscus()
    if cul == "primavara" :
        assert True
    else: 
        assert False

def test_clasificare_hibiscus():
    cul = bflori.clasificare_hibiscus()
    if cul == "sabdariffa" :
        assert True
    else: 
        assert False             
