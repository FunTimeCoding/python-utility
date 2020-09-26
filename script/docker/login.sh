#!/bin/sh -e

# shellcheck source=/dev/null
. "${HOME}/.virtualization-tools.sh"
docker login --username "${PRIVATE_REGISTRY_USERNAME}" --password "${PRIVATE_REGISTRY_PASSWORD}" "${PRIVATE_REGISTRY_SERVER}"
