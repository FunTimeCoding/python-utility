#!/bin/sh -e

WORKFLOW_DIRECTORY="${HOME}/Library/Application Support/Alfred/Alfred.alfredpreferences/workflows"

for DIRECTORY in "${WORKFLOW_DIRECTORY}"/*; do
    NAME=$(defaults read "${DIRECTORY}/info.plist" name)
    IDENTIFIER=$(basename "${DIRECTORY}")
    echo "${NAME} ${IDENTIFIER}"
done
