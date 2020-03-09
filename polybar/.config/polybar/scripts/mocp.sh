#!/bin/sh

if [ "$(mocp -Q %state)" != "STOP" ];then
    SONG=$(mocp -Q %song)
    TIMELEFT=$(mocp -Q %tl)

    if [ -n "$SONG" ]; then
        echo "$SONG - $(mocp -Q %album)"
    else
        BASE=$(basename "$(mocp -Q %file)" .mp3)
	echo "$TIMELEFT $BASE"
    fi
else
    echo ""
fi
