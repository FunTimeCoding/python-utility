import pytest

from python_utility.custom_argument_parser import CustomArgumentParser


def test_custom_argument_parser() -> None:
    parser = CustomArgumentParser()

    with pytest.raises(SystemExit):
        parser.error(message='test')
