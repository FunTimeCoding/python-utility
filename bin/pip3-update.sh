#!/bin/sh -e

PACKAGES=$(pip3 list --outdated --format json | jq --raw-output .[].name)

if [ "${PACKAGES}" = '' ]; then
    exit 0
fi

echo "pip3 updates:"
echo "${PACKAGES}"
echo "Update? [y/N]"
read -r READ

if [ ! "${READ}" = y ]; then
    exit 0
fi

for PACKAGE in ${PACKAGES}; do
    pip3 install --upgrade "${PACKAGE}"
done
