#!/bin/sh -e

if [ ! "${VIRTUAL_ENV}" = '' ]; then
    # shellcheck source=/dev/null
    . "${HOME}/venv/bin/activate"
fi

PACKAGES=$(pip list --outdated --format json | jq --raw-output .[].name)

if [ "${PACKAGES}" = '' ]; then
    exit 0
fi

echo "pip updates:"
echo "${PACKAGES}"
echo "Update? [y/N]"
read -r READ

if [ ! "${READ}" = y ]; then
    exit 0
fi

for PACKAGE in ${PACKAGES}; do
    pip install --upgrade "${PACKAGE}"
done
