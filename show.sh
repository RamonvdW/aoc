#!/bin/bash

#  Copyright (c) 2024 Ramon van der Winkel.
#  All rights reserved.
#  Licensed under BSD-3-Clause-Clear. See LICENSE file for details.

MY_MEMBER_NR="4224695"

JSON=$(ls -1t *json | head -1)
#echo "$JSON"
python3 ./leaderboard.py "$JSON" "$MY_MEMBER_NR" $*

# end of file

