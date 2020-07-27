#!/bin/sh -e

PACKAGE="${1}"

if [ "${PACKAGE}" = "" ]; then
    echo "Usage: ${0} PACKAGE"

    exit 1
fi

ITEMS=$(pip3 show "${PACKAGE}" | grep Requires | sed 's/Requires: //g; s/,//g')

for ITEM in ${ITEMS}; do
    pip3 uninstall --yes "${ITEM}"
done
