from python_utility.python_utility import PythonUtility


def test_return_code():
    application = PythonUtility()
    assert application.run() == 0
