#!/bin/sh -e

docker build --tag python-utility-snapshot .
# Show size
docker image ls python-utility-snapshot
