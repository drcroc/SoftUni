from project.album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        # if any(album.name in self.name for album in self.albums):
        if album.name in [x.name for x in self.albums]:
            return f'Band {self.name} already has {album.name} in their library.'

        self.albums.append(album)
        return f'Band {self.name} has added their newest album {album.name}.'

    def remove_album(self, album_name: str):
        for pos, name in enumerate(self.albums):
            if name.name == album_name:
                if name.published:
                    return f'Album has been published. It cannot be removed.'

                self.albums.pop(pos)
                return f'Album {album_name} has been removed.'

        return f'Album {album_name} is not found.'

    def details(self):
        text = f"Band {self.name}\n"

        for albums_obj in self.albums:
            text += albums_obj.details()
        return text