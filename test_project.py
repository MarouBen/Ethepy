from forecast import Get_coin,Get_duration
import pytest


def test_Get_coin():
    assert Get_coin("BTC") == ("bitcoin","BTC")
    assert Get_coin("btc") == ("bitcoin","BTC")
    assert Get_coin("Binance") == ("binance","BNB")
    with pytest.raises(SystemExit):
        Get_coin("cat")
    with pytest.raises(SystemExit):
        Get_coin("123")

def test_Get_duration():
    assert Get_duration("12") == 12*30
    with pytest.raises(SystemExit):
        assert Get_duration("dog") == "Invalid number of days"
    with pytest.raises(SystemExit):
        assert Get_duration("1c1") == "Invalid number of days"
    with pytest.raises(SystemExit):
        assert Get_duration("") == "Invalid number of days"
    
