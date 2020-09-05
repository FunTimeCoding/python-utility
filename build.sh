#!/bin/sh -e

# TODO: Integrate the spreadsheet service into a web end point
# TODO: Mount service_account.json to the right place
docker build --tag python-utility-snapshot .
# Show size
docker image ls python-utility-snapshot
