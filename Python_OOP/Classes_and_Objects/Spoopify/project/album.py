from project.song import Song


class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        self.songs = songs
        self.published = False
        self.songs = [x for x in songs]

    def add_song(self, new_song: Song):
        if self.published:
            return f'Cannot add songs. Album is published.'

        if new_song.single:
            return f"Cannot add {new_song.name}. It's a single"

        if any(x.name == new_song.name for x in self.songs):
            return f"Song is already in the album."

        self.songs.append(new_song)

        return f"Song {new_song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        for pos, son in enumerate(self.songs):
            if son.name == song_name:
                if self.published:

                    return f"Cannot remove songs. Album is published."

                self.songs.pop(pos)

                return f"Removed song {song_name} from album {self.name}."

        return f"Song is not in the album."

    def publish(self):
        if self.published:
            return f'Album {self.name} is already published.'

        self.published = True
        return f'Album {self.name} has been published.'

    def details(self):
        text = f"Album {self.name}\n"

        for song_obj in self.songs:
            text += f"== {song_obj}\n"

        return text
