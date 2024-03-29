# from math import ceil


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        # return cls(ceil(photos_count / 4))
        return cls((photos_count // 4))

    def add_photo(self, label: str):
        for page in range(len(self.photos)):
            if len(self.photos[page]) < 4:
                self.photos[page] += 1
                self.photos[page].append(label)

                return f'{label} photo added successfully on page {page + 1} slot {len(self.photos[page])}'

            return "No more free slots"

    def display(self):
        output = ["-----------"]
        for page in range(len(self.photos)):
            photo_count = len(self.photos[page])
            if photo_count > 0:
                pics = "[] " * photo_count
            else:
                pics = ""
            output.append(pics.rstrip())
            output.append("-----------")
        return '\n'.join(output)

