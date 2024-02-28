from src import select_execution

def test_sort_execution():

  data = select_execution.sort_execution()
  assert type(select_execution.sort_execution()) == list
  for d in data:
    assert d['state'] == 'EXECUTED'
