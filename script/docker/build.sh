#!/bin/sh -e

docker images | grep --quiet funtimecoding/python-utility && FOUND=true || FOUND=false

if [ "${FOUND}" = true ]; then
    docker rmi funtimecoding/python-utility
fi

docker build --tag funtimecoding/python-utility .
