#!/bin/sh

if [ "$(mocp -Q %state)" != "STOP" ];then
    SONG=$(mocp -Q %song)
        
    if [ -n "$SONG" ]; then
        echo "$SONG - $(mocp -Q %album)"
    else
        basename "$(mocp -Q %file)" .mp3
    fi
else
    echo ""
fi
