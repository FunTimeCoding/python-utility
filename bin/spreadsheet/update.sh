#!/bin/sh -e

SEARCH="${1}"
REPLACE="${2}"
OFFSET="${3}"

if [ "${SEARCH}" = '' ] || [ "${REPLACE}" = '' ]; then
    echo "Usage: ${0} SEARCH REPLACE [OFFSET]"
    echo "Example: ${0} Jane 2020-01-01"
    echo "This puts 2020-01-01 into the cell next to Jane."
    echo "Default offset is 1"

    exit 1
fi

if [ "${OFFSET}" = '' ]; then
    OFFSET='1'
fi

BODY=$(printf '{"search":"%s","replace":"%s","x-offset":%d}' "${SEARCH}" "${REPLACE}" "${OFFSET}")
ADDRESS=$(ifdata -pa docker0)
curl --silent --request POST --header 'Content-Type: application/json' --data "${BODY}" "http://${ADDRESS}:8080/spreadsheet"
