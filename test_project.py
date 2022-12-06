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
