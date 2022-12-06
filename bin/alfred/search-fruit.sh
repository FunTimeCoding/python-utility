#!/bin/sh -e

DIRECTORY=$(dirname "${0}")
SCRIPT_DIRECTORY=$(cd "${DIRECTORY}" || exit 1; pwd)
MATCH="${1}"

if [ "${MATCH}" = '' ]; then
    echo "Usage: ${0} MATCH"

    exit 1
fi

WORKFLOW_PATH=$("${SCRIPT_DIRECTORY}/workflow-path.sh" fruit)
docker run --interactive --tty --rm \
	--entrypoint /usr/src/app/bin/alfred/search-fruit.py \
	--volume "${HOME}/src/python-utility/bin:/usr/src/app/bin" \
	--volume "${WORKFLOW_PATH}/info.plist:/usr/src/app/info.plist" \
	--volume "${HOME}/src/python-utility/tests/fixture/fruit.txt:/usr/src/app/tests/fixture/fruit.txt" \
	python-utility-snapshot "${MATCH}"
