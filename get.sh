#!/bin/bash

#  Copyright (c) 2024 Ramon van der Winkel.
#  All rights reserved.
#  Licensed under BSD-3-Clause-Clear. See LICENSE file for details.

# copy "session" cookie content from your browser and put here
SESSION="53616c7465645f5f2a81f9d9f3cc540f286543d85e36e020847c77e8317d6a24201f91e2f1578ad5c45c1549f9c3141cb8609e015b7addd1b0633ea3d044f7fc"

STAMP=$(date +"%Y%m%d_%H%M")
FNAME="${STAMP}_leaderboard.json"
URL="https://adventofcode.com/2024/leaderboard/private/view/960233.json"

wget --header="Cookie: session=$SESSION" "$URL" -O "$FNAME"
echo "Created $FNAME"

# end of file

