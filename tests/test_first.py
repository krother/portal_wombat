
from portal_wombat.dummy import get_answer


def test_get_answer():
    assert get_answer() == 42
    