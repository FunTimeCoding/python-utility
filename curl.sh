#!/bin/sh -e

#curl --silent --request POST --header 'Content-Type: application/json' --data '{"search":"foo","replace":"123","x-offset":1}' http://localhost:8080/spreadsheet
curl --silent --request POST --header 'Content-Type: application/json' --data '{"search":"foo","replace":"123","x-offset":1}' http://172.17.0.2:8080/spreadsheet
