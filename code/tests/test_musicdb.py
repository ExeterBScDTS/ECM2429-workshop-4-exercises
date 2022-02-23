import pytest
import musicdb


@pytest.fixture
def gui():
    return musicdb.MusicDB()


def test_MusicDB():
    assert True
