#!/bin/bash

#  Copyright (c) 2024 Ramon van der Winkel.
#  All rights reserved.
#  Licensed under BSD-3-Clause-Clear. See LICENSE file for details.

# copy "session" cookie content from your browser and put here
# (use F12, application, cookies, session)
SESSION="53616c7465645f5f2a81..."

STAMP=$(date +"%Y%m%d_%H%M")
FNAME="${STAMP}_leaderboard.json"
URL="https://adventofcode.com/2024/leaderboard/private/view/960233.json"

wget --header="Cookie: session=$SESSION" "$URL" -O "$FNAME"
echo "Created $FNAME"

# end of file

