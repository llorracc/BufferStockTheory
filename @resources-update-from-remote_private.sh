#!/bin/bash
# Pull down the latest @resources and replace the existing one with it
@resources/bash/@resources-update-from-remote.sh "$(realpath $(dirname $0))"

