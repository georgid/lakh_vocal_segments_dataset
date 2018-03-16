####### imports and scripts (from http://colinraffel.com/projects/lmd/)

# Imports
import numpy as np
import pretty_midi
# import mir_eval.display
#import tables
import os
import json
import csv
import sys

# Local path constants
DATA = 'data'
RESULTS_PATH = '../'
# Path to the file match_scores.json distributed with the LMD
SCORE_FILE = os.path.join(RESULTS_PATH, 'match_scores.json')

# Utility functions for retrieving paths
def msd_id_to_dirs(msd_id):
    """Given an MSD ID, generate the path prefix.
    E.g. TRABCD12345678 -> A/B/C/TRABCD12345678"""
    return os.path.join(msd_id[2], msd_id[3], msd_id[4], msd_id)

def msd_id_to_mp3(msd_id):
    """Given an MSD ID, return the path to the corresponding mp3"""
    return os.path.join(DATA, 'msd', 'mp3',
                        msd_id_to_dirs(msd_id) + '.mp3')

def msd_id_to_h5(h5):
    """Given an MSD ID, return the path to the corresponding h5"""
    return os.path.join(RESULTS_PATH, 'lmd_matched_h5',
                        msd_id_to_dirs(msd_id) + '.h5')

def get_midi_path(msd_id, midi_md5, kind):
    """Given an MSD ID and MIDI MD5, return path to a MIDI file.
    kind should be one of 'matched' or 'aligned'. """
    return os.path.join(RESULTS_PATH, 'lmd_{}'.format(kind),
                        msd_id_to_dirs(msd_id), midi_md5 + '.mid')

def get_best_MIDI(msd_id):
    '''
    grab a MIDI for a given MSD track ID.
    @author georgi, adapted from  craffel
    
    '''
    with open(SCORE_FILE) as f:
        scores = json.load(f)

        # Grab the dictionary of MIDI matches for a trackID 
    if msd_id not in scores:
        sys.exit('{} is not matched'.format(msd_id))
    
    pretty_midis_matched = []
    
#     ######### get MIDI from the matches and check score confidence values
    max_score_aligned_MIDI = -1
    midi_md5_max = -1
    for midi_md5, score in scores[msd_id].items():
        print '  {} with confidence score {}'.format(midi_md5, score)
        
        
        # Construct the path to the aligned MIDI
        aligned_midi_path = get_midi_path(msd_id, midi_md5, 'aligned')
        # Load/parse the MIDI file with pretty_midi
        pm = pretty_midi.PrettyMIDI(aligned_midi_path)
        
        pretty_midis_matched.append(pm)

        if score > max_score_aligned_MIDI:
            midi_md5_max = midi_md5
            max_score_aligned_MIDI = score
            pm_max = pm

        
    if midi_md5_max == -1:
        sys.exit('no MIDI match found for midi {}'.format(midi_md5))


    return pm_max, pretty_midis_matched


d

def check_vocal_midi(midi):
    '''
    check which midis have a vocal channel 
    '''
    WHICH_CHANNEL_VOCAL = -1
    for i, instrument in enumerate(midi.instruments):
        
        if 'vocals' in instrument.name or 'vocal' in instrument.name  or 'MELODY' in instrument.name or 'Melody' in instrument.name or instrument.program == 75:
            WHICH_CHANNEL_VOCAL = i; break
    return WHICH_CHANNEL_VOCAL


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('usage: {} <MSD_track_ID>'.format(sys.argv[0]))

    MSD_ID = sys.argv[1]
    best_midi, all_midis_matched = get_best_MIDI(MSD_ID)

    #  check for each track separately where is the vocal
    WHICH_CHANNEL_VOCAL = check_vocal_midi(best_midi)
    if WHICH_CHANNEL_VOCAL != -1:
        print ('vocal channel {} found in midi {}'.format(WHICH_CHANNEL_VOCAL, best_midi) )

    else:    
        for midi in all_midis_matched:
            WHICH_CHANNEL_VOCAL = check_vocal_midi(midi)
            if WHICH_CHANNEL_VOCAL != -1:
                print('vocal channel {} found in midi {}'.format(WHICH_CHANNEL_VOCAL, midi) )
                break
    if WHICH_CHANNEL_VOCAL == -1:
        print 'no vocal channel found for track ', MSD_ID, ' please listen to MIDI channels'
    # print midi.instruments