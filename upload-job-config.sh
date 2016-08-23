#!/bin/sh -e

~/Code/Personal/jenkins-tools/bin/delete-job.sh python-utility || true
~/Code/Personal/jenkins-tools/bin/put-job.sh python-utility job.xml
