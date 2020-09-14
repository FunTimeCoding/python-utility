from python_utility.user_interface import UserInterface


def test_user_interface() -> None:
    user_interface = UserInterface(screen=None)
    assert user_interface.run() == 1
