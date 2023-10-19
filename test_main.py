import main
import logging

def test_get_level():
    assert main.get_level("warning") == logging.WARNING
    assert main.get_level("WaRning") == logging.WARNING
    assert main.get_level("azerty") == main.DEFAULT_LEVEL