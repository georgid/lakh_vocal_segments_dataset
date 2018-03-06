from difflib import SequenceMatcher

#f_hans = open("Hansens.dat","r")
# f_mauch = open("Mauchs.dat","r")
#content = f_hans.readlines()
# content = f_mauch.readlines()

# data = []
# for line in content:
#     data.append(line.strip().upper().split(";"))

#f_hans.close()
# f_mauch.close()

entry = ['abba', 'dancing']

#Check MSD
with open("unique_tracks.txt","r") as f_msd:
    line_no = 0
    for line in f_msd.readlines():
        line_no+=1
        if line != "\n":
            msdArtist = line.replace("\\","").strip().upper().split("<SEP>")[2]
            msdTitle = line.replace("\\","").strip().upper().split("<SEP>")[3]
            s0 = SequenceMatcher(None,entry[0],msdArtist)
            s1 = SequenceMatcher(None,entry[1],msdTitle)
            if s0.ratio() > 0.3 and s1.ratio() > 0.3:
                print(str(line_no) + ": " + line.strip() + " | " + entry[0] + ";" + entry[1])
