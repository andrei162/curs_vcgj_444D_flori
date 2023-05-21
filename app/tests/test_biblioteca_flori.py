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
        

def test_culoare_Orhidee():
    cul = bflori.culoare_Orhidee()
    if cul == "Multicolora" : 
        assert True
    else: 
        assert False
        

def test_anotimp_Orhidee():
    cul = bflori.anotimp_Orhidee()
    if cul == "Primavara" :
        assert True
    else: 
        assert False

def test_clasificare_Orhidee():
    cul = bflori.clasificare_Orhidee()
    if cul == "Decorativa" :
        assert True
    else: 
        assert False
