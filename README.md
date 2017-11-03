
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

- song from the datasets used in [MIREX Automatic_Lyrics-to-Audio_Alignment](http://www.music-ir.org/mirex/wiki/2017:Automatic_Lyrics-to-Audio_Alignment). Note that this gives initial list of songs for cross-reference, but could be extended with any other songs.
- has correctly linked MIDI (we pick the MIDI for the best match and keep the track only if it onsets are acceptably small off)
- has predominant singing voice
- has some clear metrical pulsation and the meter is 4/4

## Steps to derive annotations
1) find recording MSD_TRACK_id in this [list](https://labrosa.ee.columbia.edu/millionsong/sites/default/files/AdditionalFiles/unique_tracks.txt) find its beginning and ending timestamp and create data/MSD_TRACK_id/exceprt.txt.

2) get match from  lakh-matched MIDI [script](https://github.com/georgid/lakh_vocal_segments_dataset/blob/master/scripts/fetch_midi.ipynb) 

3) derive singing voice note annotations  - same script from 2) (find manually the number of the MIDI channel for singing voice). Optionally, doing in advance  an annotation of segments with singing voice is helpful.

4) derive beat annotations - same script from 2) (find manually the number of the MIDI channel for percussion)

5) verify annotations of note onsets and beats. Correct manually some imprecise vocal annotations. We do in [Sonic Visualiser](http://www.sonicvisualiser.org/). For this purpose .sv files are provided

- put the audio for MSD_TRACK_id in data/MSD_TRACK_id (a local copy of MSD is [at mtg's data server ](mtg.upf.edu at /mnt/compmusic/mtgstorage/scratch/msd-audio/ )
- sh scripts/open_in_sv.sh MSD_TRACK_id


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
