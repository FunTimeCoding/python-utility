#!/bin/sh -e

# shellcheck source=/dev/null
. "${HOME}/.virtualization-tools.sh"
echo "${PRIVATE_REGISTRY_PASSWORD}" | docker login --username "${PRIVATE_REGISTRY_USERNAME}" --password-stdin "${PRIVATE_REGISTRY_SERVER}"
