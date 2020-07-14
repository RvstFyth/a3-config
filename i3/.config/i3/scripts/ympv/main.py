#!/usr/bin/env python

import os
import subprocess
import sys


def main():
    if len(sys.argv) == 1:
        yt_url = new_task = subprocess.getoutput('rofi -dmenu -input /dev/null -p "YT url: " -lines 0')
        if yt_url != '':
            os.system('killall mpv')
            # TODO: use umpv not mpv.
            os.system("mpv {} --no-video --shuffle".format(yt_url)) 


def list():
    print('Show list blablabla')

if __name__ == "__main__":
    main()