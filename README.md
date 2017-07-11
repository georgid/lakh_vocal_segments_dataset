
=   =lakh-vocal-onsets==

Singing voice with annotations of vocal onsets,  based on the matched MIDI from http://colinraffel.com/projects/lmd/  


## Possible use tasks:
- vocal onset detection
- vocal transcription
not suitable for offset detection as we did not pay attention to length of pitches

list of the songs in the file list_MSD_ids

## Criteria for inclusion in dataset: 

- from the dataset used in [MIREX Automatic_Lyrics-to-Audio_Alignment](http://www.music-ir.org/mirex/wiki/2017:Automatic_Lyrics-to-Audio_Alignment) and from the dataset presented in this paper
- has correctly linked MIDI (picked up the MIDI for the best match and verified onset lications by listening)
- has predominant singing voice
- has percussive intruments
- the meter is 4/4

## Steps to derive annotations
1) find recording MSD_TRACK_id
https://labrosa.ee.columbia.edu/millionsong/sites/default/files/AdditionalFiles/unique_tracks.txt

2) get match from  lakh-matched MIDI [script](https://github.com/georgid/lakh_vocal_segments_dataset/blob/master/scripts/fetch_midi.ipynb) 

3) get note annotations  - same script from 2) 

4) get beat annotations - same script from 2)

5) validate annotations in Sonic Visualiser

- put the audio for MSD_TRACK_id (local copy at mtg.upf.edu at /mnt/compmusic/mtgstorage/scratch/msd-audio/) in data/MSD_TRACK_id
- sh scripts/open_in_sv.sh MSD_TRACK_id

### observations for excluded tracks : 
NELLY FORTADO MSD version has no voice
I kissed a girl is in 2/4, all the rest is 4/4
viva la vida not in MSD
CLOCKS has almost no voice in MSD
rehab has no vocal track in MIDI


### observations for included tracks
smells like has a lot of same-pitch onsets
call me - the onsets are on offbeats mostly
bangles and sunrise have no percussive instruments 

==== Citation =======
TODO

