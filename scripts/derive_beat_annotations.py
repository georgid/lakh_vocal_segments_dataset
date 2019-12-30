
import sys
import csv
import pretty_midi

def derive_beat_annotation(midi):
    '''
    from http://nbviewer.jupyter.org/github/craffel/midi-dataset/blob/master/Tutorial.ipynb
    '''
    # Retrieve the beats and downbeats from pretty_midi
    # Note that the beat phase will be wrong until the first time signature change after 0s
    # So, let's start beat tracking from that point
    first_ts_after_0 = [ts.time for ts in midi.time_signature_changes if ts.time > 0.][0]
    # Get beats from pretty_midi, supplying a start time
    beats = midi.get_beats(start_time=first_ts_after_0)
    # .. downbeats, too
    downbeats = midi.get_downbeats(start_time=first_ts_after_0)
    return beats, downbeats


def write_beats_to_file(beats, msd_id):
    '''
    write as csv file in format of MIR_eval.io.labeled_event
    Assumes in 4/4 and that first beat is downbeat (beat 1)
    
    '''
    URI_MSD_ID = os.path.join(RESULTS_PATH, DATA, msd_id )
    if not os.path.exists(URI_MSD_ID):
        os.makedirs(URI_MSD_ID)
        
    URI_notes_aligned_output = os.path.join(URI_MSD_ID, msd_id + '.beats_tab') # convetion name for this repo 
    
     
    BEATS_PER_BAR = 4
    ### write to output file
    f = open(URI_notes_aligned_output,'wb')
    writer = csv.writer(f, delimiter='\t')
    
    beat_num = 0 # assume starts at 1
    for beat_ts in beats: # read intervals

        row = [beat_ts + 0.1] # beat time
        beat_num= (beat_num  + 1) % BEATS_PER_BAR
        if beat_num == 0: beat_num =+  BEATS_PER_BAR # show last beat (e.g. 4) instead of 0
        row.append(beat_num) # beat number

        writer.writerow(row)

    f.close()
    print 'written file ' + URI_notes_aligned_output

if __name__ == '__main__':
    
    if len(sys.argv) != 3:
        sys.exit('usage: {} <midi> <MSD_track_ID>'.format(sys.argv[0]))

    midi_path = sys.argv[1]
    pm = pretty_midi.PrettyMIDI(midi_path)
    MSD_ID = sys.argv[2]
    beats, downbeats = derive_beat_annotation(pm)

    write_beats_to_file (beats, MSD_ID)