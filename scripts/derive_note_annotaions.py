import sys
import csv

def derive_note_annotation(midi, WHICH_CHANNEL_VOCAL):
    '''
    midi:  object of pretty MIDI library 
    WHICH_CHANNEL_VOCAL: channel of vocal, has to be checked for each track separately
    
    from http://nbviewer.jupyter.org/github/craffel/midi-dataset/blob/master/Tutorial.ipynb
    '''

    vocal_channel = midi.instruments[WHICH_CHANNEL_VOCAL]
    intervals = np.array([[note.start, note.end] for note in vocal_channel.notes]) # note intervals
    notes = np.array([note.pitch for note in vocal_channel.notes]) # MIDI numbers
    return intervals, notes 

def write_notes_to_file(intervals, notes, msd_id):
    '''
    write as csv file in format of MIR_eval.io.labeled_intervals

    '''
    
    URI_MSD_ID = os.path.join(RESULTS_PATH, DATA, msd_id )
    if not os.path.exists(URI_MSD_ID):
        os.makedirs(URI_MSD_ID)
    URI_notes_aligned_output = os.path.join(URI_MSD_ID, 'alignedNotes_vocal.txt') # convetion name for this repo 
    
    ### write to output file
    f = open(URI_notes_aligned_output,'wb')
    writer = csv.writer(f, delimiter='\t')

    for interval, note in zip(intervals, notes): # read intervals

        row = [interval[0]] # onset time
        row.append(interval[1]-interval[0]) # duration
        row.append(note) # MIDI number
        # row.append(0) # satisfy sonic visualiser's format

        writer.writerow(row)

    f.close()
    print 'written file ' + URI_notes_aligned_output

if __name__ == '__main__':

    if len(sys.argv) != 4:
        sys.exit('usage: {} <midi> <MSD_track_ID> <WHICH_CHANNEL_VOCAL>'.format(sys.argv[0]))

    midi = sys.argv[1]
    MSD_ID = sys.argv[2]
    WHICH_CHANNEL_VOCAL = sys.argv[3] 
    intervals, notes  = derive_note_annotation(midi, WHICH_CHANNEL_VOCAL)
    write_notes_to_file(intervals, notes, MSD_ID) 