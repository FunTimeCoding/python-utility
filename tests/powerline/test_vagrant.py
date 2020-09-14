from os import mkdir, rmdir, getcwd, remove
from os.path import join, exists
from shutil import rmtree

import pytest

from python_utility.command_process import CommandFailed
from python_utility.powerline.vagrant import VagrantSegment

TEMPORARY_DIRECTORY = '/tmp/python_utility'


# TODO: The vagrant subprocess cannot access the temporary directory. What is
#  a better practice? The insecure directory above accepted on SonarQube for
#  now.
# TEMPORARY_DIRECTORY = tempfile.TemporaryDirectory(dir='/tmp').name


def test_create_test_directory() -> None:
    rmtree(TEMPORARY_DIRECTORY)
    mkdir(TEMPORARY_DIRECTORY)
    assert exists(TEMPORARY_DIRECTORY)


def test_vagrant_file_exists() -> None:
    assert VagrantSegment.vagrant_file_exists(getcwd())
    assert not VagrantSegment.vagrant_file_exists(TEMPORARY_DIRECTORY)


def test_vagrant_status_raises_on_empty_directory() -> None:
    with pytest.raises(CommandFailed):
        VagrantSegment.vagrant_status(TEMPORARY_DIRECTORY)


def test_callable_no_vagrant_directory() -> None:
    segment = VagrantSegment()
    segment_info = {
        'shortened_path': TEMPORARY_DIRECTORY
    }
    assert segment(None, segment_info, None) == [{
        'contents': '.vagrant directory not found',
        'highlight_groups': ['information:regular'],
    }]


def test_callable_no_vagrant_file() -> None:
    segment = VagrantSegment()
    segment_info = {
        'shortened_path': TEMPORARY_DIRECTORY
    }
    vagrant_directory = join(TEMPORARY_DIRECTORY, '.vagrant')
    mkdir(vagrant_directory)
    assert segment(None, segment_info, None) == [{
        'contents': 'Vagrantfile not found',
        'highlight_groups': ['information:regular'],
    }]
    rmdir(vagrant_directory)


def test_callable_vagrant_file_and_directory_exist() -> None:
    segment = VagrantSegment()
    segment_info = {
        'shortened_path': TEMPORARY_DIRECTORY
    }
    vagrant_directory = join(TEMPORARY_DIRECTORY, '.vagrant')
    mkdir(vagrant_directory)
    with open(join(TEMPORARY_DIRECTORY, 'Vagrantfile'), 'w') as fp:
        pass
    assert segment(None, segment_info, None) == [{
        'contents': 'not created',
        'highlight_groups': ['information:regular'],
    }]
    rmtree(vagrant_directory)


def test_vagrant_directory_exists() -> None:
    vagrant_directory = join(TEMPORARY_DIRECTORY, '.vagrant')
    mkdir(vagrant_directory)
    assert VagrantSegment.vagrant_directory_exists(TEMPORARY_DIRECTORY)
    rmdir(vagrant_directory)
    assert not VagrantSegment.vagrant_directory_exists(TEMPORARY_DIRECTORY)


def test_remove_test_directory() -> None:
    rmtree(TEMPORARY_DIRECTORY)
    assert not exists(TEMPORARY_DIRECTORY)
