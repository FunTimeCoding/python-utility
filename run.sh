#!/bin/sh -e

docker run --rm --volume ~/.config/gspread:/root/.config/gspread --volume ~/.python-utility.yaml:/root/.python-utility.yaml python-utility-snapshot
