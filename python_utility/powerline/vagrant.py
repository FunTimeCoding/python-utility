from __future__ import (
    unicode_literals,
    division,
    absolute_import,
    print_function
)

from os import path
from os.path import expanduser, join

from powerline.segments import Segment, with_docstring
from powerline.theme import requires_segment_info, requires_filesystem_watcher

from python_utility.command_process import CommandProcess


@requires_filesystem_watcher
@requires_segment_info
class VagrantSegment(Segment):
    divider_highlight_group = None

    def __call__(self, pl, segment_info, create_watcher):
        current_directory = expanduser(segment_info['shortened_path'])
        vagrant_directory_exists = path.exists(
            join(current_directory, '.vagrant')
        )
        vagrant_file_exists = path.exists(
            join(current_directory, 'Vagrantfile')
        )

        if vagrant_directory_exists and vagrant_file_exists:
            process = CommandProcess(['vagrant', 'status'], current_directory)
            output = 'unknown'

            for line in process.output.splitlines():
                if 'not created' in line:
                    output = 'not created'

                    break
                elif 'poweroff' in line:
                    output = 'poweroff'

                    break
                elif 'running' in line:
                    output = 'running'

                    break
                elif 'saved' in line:
                    output = 'saved'

                    break

            result = [{
                'contents': output,
                'highlight_groups': ['information:regular'],
            }]
        else:
            result = []

        return result


status = with_docstring(VagrantSegment(), '''Return a custom segment.''')
