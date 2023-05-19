import lib.biblioteca_flori as bflori

def test_culoare_bonsai():
    cul = bflori.culoare_bonsai()
    if cul == "alb" : 
        assert True
    else: 
        assert False
        

def test_anotimp_bonsai():
    cul = bflori.anotimp_bonsai()
    if cul == "vara" :
        assert True
    else: 
        assert False

def test_clasificare_bonsai():
    cul = bflori.clasificare_bonsai()
    if cul == "toxic" :
        assert True
    else: 
        assert False
