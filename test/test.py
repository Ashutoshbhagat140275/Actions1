from src.app import add,sub,mul,div

def test_add():
    assert add(-1,2)==1
    assert add(0,0)==1
    assert add(9,10)==19

def test_sub():
    assert sub(-1,1)==-2
    assert sub(1,1)==0
    assert sub(10,12)==22

def test_mul():
    assert mul(1,0)==0
    assert mul(2,2)==4
    assert mul(4,-1)==-4

def test_div():
    assert div(2,4)==0.5
    assert div(6,3)==2
    assert div(4,10)==2.5
    with pytest.raises(ValueError):
        div(1,0)