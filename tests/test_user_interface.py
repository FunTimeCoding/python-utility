from python_utility.user_interface import UserInterface


def test_user_interface() -> None:
    assert UserInterface(screen=None).run() == 1
