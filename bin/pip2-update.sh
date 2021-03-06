#!/bin/sh -e

PACKAGES=$(pip2 list --outdated --format json | jq --raw-output .[].name)

if [ "${PACKAGES}" = '' ]; then
    exit 0
fi

echo "pip2 updates:"
echo "${PACKAGES}"
echo "Update? [y/N]"
read -r READ

if [ ! "${READ}" = y ]; then
    exit 0
fi

for PACKAGE in ${PACKAGES}; do
    pip2 install --upgrade "${PACKAGE}"
done
