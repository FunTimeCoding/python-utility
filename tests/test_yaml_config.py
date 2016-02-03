from os import remove
from os.path import isfile

from python_utility.yaml_config import YamlConfig


def test_set_get_remove():
    config = YamlConfig()

    # should be empty
    assert config.contains('my-key') is False
    assert config.get('my-key') == ''

    # should contain something
    config.set('my-key', 'my-value')
    assert config.contains('my-key') is True
    assert config.get('my-key') == 'my-value'

    # should remove something
    config.remove('my-key')
    assert config.contains('my-key') is False
    assert config.get('my-key') == ''


def test_save():
    file = '/tmp/example.yml'

    # file should not exist
    if isfile(file):
        remove(file)
    assert isfile(file) is False

    # file should be created on save
    config = YamlConfig(file)
    assert isfile(file) is False
    config.save()
    assert config.exists() is True
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
    output_file = YamlConfig(file)
    output_file.set('my-key', 'my-value')
    output_file.save()

    # file should contain something
    input_file = YamlConfig(file)
    assert input_file.get('my-key') == 'my-value'

    # file should be gone
    remove(file)
    assert isfile(file) is False
