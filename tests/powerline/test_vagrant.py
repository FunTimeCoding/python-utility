import os

import pytest

from python_utility.command_process import CommandFailed
from python_utility.powerline.vagrant import VagrantSegment


def test_vagrant_file_exists() -> None:
    assert VagrantSegment.vagrant_file_exists(os.getcwd())
    assert not VagrantSegment.vagrant_file_exists('/tmp')


def test_vagrant_directory_exists() -> None:
    os.mkdir('/tmp/.vagrant')
    assert VagrantSegment.vagrant_directory_exists('/tmp')
    os.rmdir('/tmp/.vagrant')
    assert not VagrantSegment.vagrant_directory_exists('/tmp')


def test_vagrant_status() -> None:
    with pytest.raises(CommandFailed):
        VagrantSegment.vagrant_status('/tmp')
