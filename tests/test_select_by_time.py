from src import select_by_time

def test_last_sel():
    assert len(select_by_time.last_sel()) == 5
    assert type(select_by_time.last_sel()) == list