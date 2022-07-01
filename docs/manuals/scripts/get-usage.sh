#!/bin/bash

set -e
set -u

FULLPATH="$1"
TARGETDIR="$2"

COMMAND=$(basename "${FULLPATH}")

USAGE=$("${FULLPATH}" --help)

sed --expression='/Usage:/,$!d' --expression='s|Usage: .*/|Usage: |' <<<"${USAGE}" > "${TARGETDIR}/${COMMAND}.txt"
