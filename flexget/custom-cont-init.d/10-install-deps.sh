#!/bin/sh
echo "[init] Installing rsync, ffmpeg, mediainfo (Alpine/apk)..."
apk add --no-cache rsync ffmpeg mediainfo
echo "[init] Done ✅"
