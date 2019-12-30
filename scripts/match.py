from difflib import SequenceMatcher
import pandas as pd
import Levenshtein
import re
import json

# 1. all Sing! partner artists
OUT_FILE_MSD = '/Users/georgid/Dropbox (Smule-EUDC)/arrs-pa_seeds_english_to_MSD'
OUT_FILE_HMX = '/Users/georgid/Dropbox (Smule-EUDC)/arrs-pa_seeds_to_Harmonix.json'

# df_pa_arrs = pd.read_csv('/Users/georgid/Dropbox (Smule-EUDC)/arrs-pa_seeds_english.csv')
df_pa_arrs = pd.read_csv('/Users/georgid/Dropbox (Smule-EUDC)/arrs-pa_seeds.csv')


# or 2. all Sing! in-house
OUT_FILE_HMX = '/Users/georgid/Dropbox (Smule-EUDC)/arrs-in_house_to_Harmonix.json'
df_pa_arrs = pd.read_csv('/Users/georgid/Dropbox (Smule-EUDC)/arrs-in_house.csv')


arr_key_to_external = {}

def match_arr_key_to_MSD(entry, arr_key):

    '''
    for entry song check by fuzzy matching on name+ artst if in MSD list 
    '''
    print('working on song: {} - {}'.format(entry[0], entry[1]))

    with open("unique_tracks.txt","r") as f_msd:
        line_no = 0
        for line in f_msd.readlines():
            line_no+=1
            if line != "\n":
                line_norm = line.replace("\\","").strip().upper().split("<SEP>")
                msdArtist = line_norm[2]
                msdTitle = line_norm[3]
                msd_id = line_norm[0]
                if match_2(msdArtist, entry[0], msdTitle, entry[1]):
                    print(str(line_no) + ": " + line.strip() + " for entry " + entry[0] + ";" + entry[1])
                    if arr_key not in arr_key_to_external:
                       arr_key_to_external[arr_key] = []
                    arr_key_to_external[arr_key].append(msd_id)
    return arr_key_to_external


def match_arr_key_to_HMX(entry, arr_key):

    '''
    for entry song check by fuzzy matching on name+ artst if in Harmonix list 
    
    entry is arrangement
    '''
    print('working on song: {} - {}'.format(entry[0], entry[1]))

    df = pd.read_csv('/Users/georgid/Downloads/metadata.csv') # from https://github.com/urinieto/harmonixset/blob/master/dataset/metadata.csv
    for idx in df.index:
            hmx_title = df['Title'][idx]
            hmx_artist = df['Artist'][idx]
            if match_2(hmx_artist, entry[0], hmx_title, entry[1]):
                    print( "Harmonix: {} - {}  Vs sing! :  + {}  - {} ".format(hmx_artist, hmx_title, entry[0],  entry[1] )   )
                    a = raw_input() # validate manually if it is a match
                    if a == 'no':
                        continue
                    if arr_key not in arr_key_to_external:
                       arr_key_to_external[arr_key] = []
                    arr_key_to_external[arr_key].append(df['File'][idx])
    return arr_key_to_external


def match_1(artist,artist1, title, title1):
    '''
    based on sequence matcher
    '''
    s0 = SequenceMatcher(None,artist,artist1)
    s1 = SequenceMatcher(None,title,title1)
    return s0.ratio() > 0.27 and s1.ratio() > 0.27

def match_2(artist,artist1, title, title1):
    '''
    based on Levenshtein distance 
    '''
    return match_Levenshtein(artist, artist1) and match_Levenshtein(title, title1)

def match_Levenshtein(a, b):
        '''
        use Levenshtein distance. Adapted from "match" in https://github.com/MTG/pycompmusic/blob/master/tools/sertanscores.py#L146
        '''
        if isinstance(a, unicode):
            a = unidecode.unidecode(a)
        if isinstance(b, unicode):
            b = unidecode.unidecode(b)

        a = a.lower()
        b = b.lower()

        # lowercase and remove all non-letters (spaces, ', -, etc)
        a = re.sub(r"[^a-z]", "", a)
        b = re.sub(r"[^a-z]", "", b)

        # if a match, return
        if a == b:
            return True

        # otherwise, do edit distance.
        # an edit of <= 3 at the end of a string counts as a match
        if len(a) > len(b):
            a, b = b, a
        # now, a is the shorter one. If a starts in b at position 0
        #  then we have the overlap at the end
        # if b.startswith(a):
        #     return True

        # Otherwise, chop both strings to the length of the shortest
        # one, and check lev distance between them for <= 3
        # b = b[:len(a)]
        return Levenshtein.distance(a, b) <= 3


if __name__ == '__main__':
    print(df_pa_arrs.columns)
    df_pa_arrs = df_pa_arrs.dropna(axis = 0, how ='any') # drop entries with any missing column 
    
    for index, row in df_pa_arrs.iterrows():
        # arr_key_matched = match_arr_key_to_MSD( [row['artist'], row['titl']], row['arr_key'])
        arr_key_matched = match_arr_key_to_HMX( [row['artist'], row['titl']], row['arr_key'])

    
    json.dump(arr_key_matched, open(OUT_FILE_HMX,"w"))
    print('written file {}'.format(OUT_FILE_HMX))
