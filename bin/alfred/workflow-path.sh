#!/bin/sh -e

DIRECTORY=$(dirname "${0}")
SCRIPT_DIRECTORY=$(cd "${DIRECTORY}" || exit 1; pwd)
WORKFLOWS=$("${SCRIPT_DIRECTORY}/show-workflows.sh")
NAME="${1}"

if [ "${NAME}" = '' ]; then
    echo "Usage: ${0} NAME"
    echo "Available:"
    echo "${WORKFLOWS}" | awk '{ print $1 }'

    exit 1
fi

WORKFLOW_NAME=''
WORKFLOW_DIRECTORY=''

while read -r WORKFLOW; do
    WORKFLOW_NAME=$(echo "${WORKFLOW}" | awk '{ print $1 }')
    WORKFLOW_DIRECTORY=$(echo "${WORKFLOW}" | awk '{ print $2 }')

    if [ "${WORKFLOW_NAME}" = "${NAME}" ]; then
        break
    fi
done <<< "${WORKFLOWS}"

if [ "${WORKFLOW_NAME}" = '' ] || [ "${WORKFLOW_DIRECTORY}" = '' ]; then
    echo "Workflow not found: ${NAME}"
    echo "${WORKFLOWS}" | awk '{ print $1 }'

    exit 1
fi

echo "${HOME}/Library/Application Support/Alfred/Alfred.alfredpreferences/workflows/${WORKFLOW_DIRECTORY}"
