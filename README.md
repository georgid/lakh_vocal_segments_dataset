
# lakh vocal segments dataset

This is a dataset of multi-instrumental recordings of pop songs (in English) with annotations transcription of singing voice,  based on the MIDI matched from the [lakh dataset](http://colinraffel.com/projects/lmd/). Created to provide real-world material for singing vocie transciption with diverse genres and singers.


## Possible use tasks:
- vocal onset detection
- transcription of singing voice into notes
- beat detection

Note that it is not suitable yet for offset detection as we did not validate the correctness of the length of aligned MIDI notes

## Folder structure
- list_MSD_ids:  list of the songs in the dataset
- scripts:  python scripts for loading data, more scripts are in the [similar repository](https://github.com/georgid/otmm_vocal_segments_dataset/tree/master/scripts)
- data: audio files. excerpt.txt gives begining and ending timestamp of the 7-digital exceprt from the complete recording. Determined manually.


## Criteria for inclusion in the dataset:

- songs from the datasets used in [MIREX Automatic_Lyrics-to-Audio_Alignment](http://www.music-ir.org/mirex/wiki/2017:Automatic_Lyrics-to-Audio_Alignment) full-listed also [here](https://docs.google.com/document/d/1bOefN9gEqYKPl7x3kmnJ1OWsjLuApza-9246qlBbMNY/edit?usp=sharing). Note that this gives initial list of songs for cross-reference, but could be extended with any other songs.
- has a linked MIDI in the lakh dataset 
- has predominant singing voice present in the 30-seconds thumbnail
- has some clear metrical pulsation and the meter is 4/4

## Steps to derive annotations
1) find recording MSD_TRACK_id from this [list](https://labrosa.ee.columbia.edu/millionsong/sites/default/files/AdditionalFiles/unique_tracks.txt).  [match](https://github.com/georgid/lakh_vocal_segments_dataset/blob/master/scripts/match.py) 
- Then derive its beginning and ending timestamp and create data/MSD_TRACK_id/exceprt.txt manually.

2) get the matched MIDI from lakh-matched MIDI [fetch_midi](https://github.com/georgid/lakh_vocal_segments_dataset/blob/master/scripts/fetch_midi.py)  (if more than one match, pick the MIDI for the best match)

3) derive singing voice note annotations  
[derive_note_annotations](https://github.com/georgid/lakh_vocal_segments_dataset/blob/master/scripts/derive_note_annotations.py) Optionally, doing in advance an annotation of vocal activity detection (VAD) segments (e.g. with singing voice present is helpful.

4) derive beat annotations - [derive_beat_annotations](https://github.com/georgid/lakh_vocal_segments_dataset/blob/master/scripts/derive_beat_annotations.py) (find manually the number of the MIDI channel for percussion)

5) verify annotations of note onsets and beats. Correct manually some imprecise vocal annotations. Could be done in [Sonic Visualiser](http://www.sonicvisualiser.org/) by opening sh [open_in_sv.sh](https://github.com/georgid/lakh_vocal_segments_dataset/blob/master/scripts/open_in_sv.sh)

- put the audio for MSD_TRACK_id in data/MSD_TRACK_id 
cp /Volumes/datasets/MTG/audio/incoming/millionsong-audio/mp3/D/W/U/$track_ID data/ 



## Scratch notes and observations on songs so far...
### observations for excluded tracks :
NELLY FORTADO MSD version has no voice
I kissed a girl is in 2/4, all the rest is 4/4
viva la vida not in MSD
CLOCKS has almost no voice in MSD
rehab has no vocal channel in MIDI


### observations for included tracks
smells like has a lot of same-pitch onsets
call me - the onsets are on offbeats mostly
bangles and sunrise have no percussive instruments


## Citation

Georgi Dzhambazov, André Holzapfel, Ajay Srinivasamurthy, Xavier Serra, Metrical-Accent Aware Vocal Onset Detection in Polyphonic Audio, In Proceedings of ISMIR 2017

## Contact

georgi (dot) dzhambazov (at) upf (dot) edu

## License
The license for annotations follows the license of [lakh dataset](http://colinraffel.com/projects/lmd/).
The audio comes form the MSD and is shared here for the purpose of crowd-annotation. However, we will remove it once we release the dataset.
