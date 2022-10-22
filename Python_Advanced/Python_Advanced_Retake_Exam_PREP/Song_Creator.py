import os


def add_songs(*songs):
    songs_dict = {}
    for song_title, song_text in songs:
        if song_title not in songs_dict.keys():
            songs_dict[song_title] = []
        songs_dict[song_title].extend(song_text)

    result = []
    for song_names, song_lyrics in songs_dict.items():
        result.append('- ' + song_names)
        if song_lyrics:
            result.extend(song_lyrics)
    return os.linesep.join(result)

