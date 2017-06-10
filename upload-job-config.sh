#!/bin/sh -e

~/src/jenkins-tools/bin/delete-job.sh python-utility || true
~/src/jenkins-tools/bin/put-job.sh python-utility job.xml
