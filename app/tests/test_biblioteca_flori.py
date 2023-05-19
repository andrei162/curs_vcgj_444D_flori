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
        
        
        
        
        

def test_culoare_liliac():
    cul = bflori.culoare_liliac()
    if cul == "mov" : 
        assert True
    else: 
        assert False
        

def test_anotimp_liliac():
    cul = bflori.anotimp_liliac()
    if cul == "primavara" :
        assert True
    else: 
        assert False

def test_clasificare_liliac():
    cul = bflori.clasificare_liliac()
    if cul == "toxic" :
        assert True
    else: 
        assert False
