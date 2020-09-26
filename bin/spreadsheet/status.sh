#!/bin/sh -e

ADDRESS=$(ifdata -pa docker0)
curl "http://${ADDRESS}:8080/status"
