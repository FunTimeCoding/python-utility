from os import mkdir, rmdir, getcwd
from os.path import join, exists

import pytest

from python_utility.command_process import CommandFailed
from python_utility.powerline.vagrant import VagrantSegment

TEMPORARY_DIRECTORY = '/tmp/python_utility'


# TODO: The vagrant subprocess cannot access the temporary directory. What is
#  a better practice? The insecure directory above accepted on SonarQube for
#  now.
# TEMPORARY_DIRECTORY = tempfile.TemporaryDirectory(dir='/tmp').name


def test_create_test_directory() -> None:
    mkdir(TEMPORARY_DIRECTORY)
    assert exists(TEMPORARY_DIRECTORY)


def test_vagrant_file_exists() -> None:
    assert VagrantSegment.vagrant_file_exists(getcwd())
    assert not VagrantSegment.vagrant_file_exists(TEMPORARY_DIRECTORY)


def test_callable() -> None:
    segment = VagrantSegment()
    power_line = None
    segment_info = {
        'shortened_path': TEMPORARY_DIRECTORY
    }
    create_watcher = None
    assert segment(power_line, segment_info, create_watcher) == [{
        'contents': '.vagrant directory not found',
        'highlight_groups': ['information:regular'],
    }]


def test_vagrant_directory_exists() -> None:
    vagrant_directory = join(TEMPORARY_DIRECTORY, '.vagrant')
    mkdir(vagrant_directory)
    assert VagrantSegment.vagrant_directory_exists(TEMPORARY_DIRECTORY)
    rmdir(vagrant_directory)
    assert not VagrantSegment.vagrant_directory_exists(TEMPORARY_DIRECTORY)


def test_vagrant_status() -> None:
    with pytest.raises(CommandFailed):
        VagrantSegment.vagrant_status(TEMPORARY_DIRECTORY)


def test_remove_test_directory() -> None:
    rmdir(TEMPORARY_DIRECTORY)
    assert not exists(TEMPORARY_DIRECTORY)
