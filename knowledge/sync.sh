#!/bin/bash
git add .
git commit -m "Auto sync $(date '+%Y-%m-%d %H:%M')"
git pull --rebase
git push
