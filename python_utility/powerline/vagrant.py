from __future__ import (
    unicode_literals,
    division,
    absolute_import,
    print_function
)

from os import path
from os.path import expanduser, join

import re

from powerline.segments import Segment, with_docstring
from powerline.theme import requires_segment_info, requires_filesystem_watcher

from python_utility.command_process import CommandProcess, CommandFailed


@requires_filesystem_watcher
@requires_segment_info
class VagrantSegment(Segment):
    NOT_CREATED_STATUS = 'not created'
    POWER_OFF_STATUS = 'poweroff'
    RUNNING_STATUS = 'running'
    SAVED_STATUS = 'saved'
    STATUSES = [
        NOT_CREATED_STATUS,
        POWER_OFF_STATUS,
        RUNNING_STATUS,
        SAVED_STATUS,
    ]
    divider_highlight_group = None

    def __call__(self, power_line, segment_info, create_watcher):
        current_directory = expanduser(segment_info['shortened_path'])

        if not VagrantSegment.vagrant_directory_exists(
                current_directory=current_directory
        ):
            contents = '.vagrant directory not found'
        elif not VagrantSegment.vagrant_file_exists(
                current_directory=current_directory
        ):
            contents = 'Vagrantfile not found'
        else:
            contents = VagrantSegment.vagrant_status(
                current_directory=current_directory
            )

        return [{
            'contents': contents,
            'highlight_groups': ['information:regular'],
        }]

    @staticmethod
    def vagrant_file_exists(current_directory: str):
        return path.exists(join(current_directory, 'Vagrantfile'))

    @staticmethod
    def vagrant_directory_exists(current_directory: str):
        return path.exists(join(current_directory, '.vagrant'))

    @staticmethod
    def vagrant_status(current_directory: str) -> str:
        try:
            result = re.sub(
                pattern=' +',
                repl=' ',
                string=CommandProcess(
                    arguments=['vagrant', 'status'],
                    path=current_directory,
                ).standard_output.splitlines()[2]
            ).strip("default ").strip(" (virtualbox)")
        except CommandFailed:
            result = 'unknown'

        return result


status = with_docstring(VagrantSegment(), '''Return a custom segment.''')
