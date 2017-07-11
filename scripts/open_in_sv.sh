#!/bin/bash

URI_LAKH_VOCAL=~/workspace//lakh_vocal_segments_dataset/data/;
MSD_ID=$1;
INPUT_AUDIO=$URI_LAKH_VOCAL/$MSD_ID/$MSD_ID.mp3;
BEATS=$URI_LAKH_VOCAL/$MSD_ID/$MSD_ID.beats_tab;
VOCAL_NOTES=$URI_LAKH_VOCAL/$MSD_ID/alignedNotes_vocal.txt;
open -a Sonic\ Visualiser $INPUT_AUDIO $VOCAL_NOTES $BEATS 
