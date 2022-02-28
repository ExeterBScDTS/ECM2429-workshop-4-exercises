#!/bin/bash

for file in */*.mp3; do 
 # Limit duration to 10 secs
 ffmpeg -t 10 -i "$file" -acodec pcm_s16le -ac 1 -ar 8000 "${file%.mp3}.wav"
done