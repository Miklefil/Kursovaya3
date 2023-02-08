from utils import get_data
import pytest



def test_get_data(test_url):
    assert len(get_data(test_url)[0]) > 0