#!/bin/sh -e

# Development mode mounts the project root so it can be edited and re-ran without rebuilding the image and recreating the container.

if [ "${1}" = --development ]; then
    DEVELOPMENT=true
else
    DEVELOPMENT=false
fi

docker ps --all | grep --quiet python-utility && FOUND=true || FOUND=false

if [ "${FOUND}" = false ]; then
    WORKING_DIRECTORY=$(pwd)

    if [ "${DEVELOPMENT}" = true ]; then
        docker create --name python-utility --volume "${WORKING_DIRECTORY}:/python-utility" funtimecoding/python-utility
    else
        docker create --name python-utility funtimecoding/python-utility
    fi

    # TODO: Specifying the entry point overrides CMD in Dockerfile. Is this useful, or should all sub commands go through one entry point script? I'm inclined to say one entry point script per project.
    #docker create --name python-utility --volume "${WORKING_DIRECTORY}:/python-utility" --entrypoint /python-utility/bin/other.sh funtimecoding/python-utility
    #docker create --name python-utility funtimecoding/python-utility /python-utility/bin/other.sh
    # TODO: Run tests this way?
    #docker create --name python-utility funtimecoding/python-utility /python-utility/script/docker/test.sh
fi

docker start --attach python-utility
