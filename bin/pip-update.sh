#!/bin/sh -e

DIRECTORY=$(dirname "${0}")
SCRIPT_DIRECTORY=$(cd "${DIRECTORY}" || exit 1; pwd)

usage()
{
    echo "Usage: ${0}"
}

# shellcheck source=/dev/null
. "${SCRIPT_DIRECTORY}/../lib/python_tools.sh"
#${SCRIPT_DIRECTORY}/pip2-update.sh
"${SCRIPT_DIRECTORY}"/pip3-update.sh
"${SCRIPT_DIRECTORY}"/venv-update.sh
