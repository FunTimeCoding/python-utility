from lib.python_utility import PythonUtility


def test_return_code():
    pu = PythonUtility()
    assert pu.run() == 0
