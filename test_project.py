from project import Get_name,Get_duration,Get_symbol
import pytest


def test_Get_symbol():
    assert Get_symbol("bitcoin") == ("BTC")
    assert Get_symbol("xrp") == ("XRP")
    assert Get_symbol("etherium") == ("ETH")
    
    with pytest.raises(SystemExit):
        Get_symbol("cat")
    with pytest.raises(SystemExit):
        Get_symbol("123")

def test_Get_duration():
    assert Get_duration("12") == 12*30
    with pytest.raises(SystemExit):
        assert Get_duration("dog") == "Invalid number of days"
    with pytest.raises(SystemExit):
        assert Get_duration("1c1") == "Invalid number of days"
    with pytest.raises(SystemExit):
        assert Get_duration("") == "Invalid number of days"
        
    
