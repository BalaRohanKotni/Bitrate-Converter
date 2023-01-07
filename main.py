import csv
import music_tag
import os
from tinytag import TinyTag
from pydub import AudioSegment

# path = "/Users/rohan/Desktop/fake-bitrates.txt"
# destination = "/Users/rohan/Desktop/"
path = input("File consisting filenames and bitrates: ")
destination = input("Destination: ")
i = 1
count = sum(1 for line in open(path))
with open(path, "r", encoding="utf8") as file:
    tsv_reader = csv.DictReader(file, delimiter="\t")
    for filepath in tsv_reader:

        filenamepath = filepath["Filepath"]
        # os.system('rm "{}"'.format(filenamepath))
        bitrate = filepath["Bitrate"]+"k"

        mp3_file_name = filenamepath[len("/Users/rohan/Music/Flac/"):]
        mp3_file_name = mp3_file_name[:-5]+".mp3"
        mp3_file_name=destination+mp3_file_name

        flac_file = AudioSegment.from_file(filenamepath)
        tags = TinyTag.get(filenamepath, image=True)

        # get tags from flac
        title = tags.title
        album = tags.album
        artist = tags.artist
        artwork = tags.get_image()

        if title == None: title = ""

        if album == None: album = ""

        if artist == None: artist = ""
        
        flac_file.export(mp3_file_name, format="mp3", bitrate=bitrate)
        mp3_file = music_tag.load_file(mp3_file_name)
        mp3_file['title'] = title
        mp3_file['album'] = album
        mp3_file['artist'] = artist
        mp3_file['artwork'] = artwork
        mp3_file.save()
        print("({}/{})          ".format(i, count),mp3_file_name, bitrate, flac_file.frame_rate, artist, title, album)
        i+=1




