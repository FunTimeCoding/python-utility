from os import remove
from os.path import isfile

from python_utility.configuration import Configuration


def test_set_get_remove() -> None:
    configuration = Configuration()

    # should be empty
    assert configuration.contains('my-key') is False
    assert configuration.get('my-key') == ''

    # should contain something
    configuration.set('my-key', 'my-value')
    assert configuration.contains('my-key') is True
    assert configuration.get('my-key') == 'my-value'

    # should remove something
    configuration.remove('my-key')
    assert configuration.contains('my-key') is False
    assert configuration.get('my-key') == ''


def test_get_nested() -> None:
    configuration = Configuration('tests/fixture/nested.yaml')

    assert configuration.contains('foo') is True
    assert configuration.get('foo')['bar'] == 'baz'


def test_save() -> None:
    file = '/tmp/example.yml'

    # file should not exist
    if isfile(file):
        remove(file)
    assert isfile(file) is False

    # file should be created on save
    configuration = Configuration(file)
    assert isfile(file) is False
    configuration.save()
    assert configuration.exists() is True
    assert isfile(file) is True

    # file should be gone
    remove(file)
    assert isfile(file) is False


def test_write_and_read():
    file = '/tmp/example.yml'

    # file should not exist
    if isfile(file):
        remove(file)
    assert isfile(file) is False

    # file should be created
    output_file = Configuration(file)
    output_file.set('my-key', 'my-value')
    output_file.save()

    # file should contain something
    input_file = Configuration(file)
    assert input_file.get('my-key') == 'my-value'

    # file should be gone
    remove(file)
    assert isfile(file) is False
