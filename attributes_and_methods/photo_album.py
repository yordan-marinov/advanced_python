import math


class PhotoAlbum:
    max_photos_per_page = 4

    def __init__(self, pages: int):
        self.pages: int = pages
        self.photos = [[] for _ in range(self.pages)]
        self.current_picture = 0
        self.max_pictures = self.pages * PhotoAlbum.max_photos_per_page

    @staticmethod
    def pages_from_photos_count(photos_count):
        return math.ceil(photos_count / PhotoAlbum.max_photos_per_page)

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(PhotoAlbum.pages_from_photos_count(photos_count))

    def current_page_of_photos(self) -> int:
        return math.ceil(
            self.current_picture / PhotoAlbum.max_photos_per_page
        ) - 1

    def is_free_slots(self):
        return self.current_picture < self.max_pictures

    def add_photo(self, label: str):
        if not self.is_free_slots():
            return "No more free spots"

        self.current_picture += 1
        self.photos[self.current_page_of_photos()].append(label)

        return f"{label} photo added successfully on page {self.current_page_of_photos() + 1} " \
               f"slot {len(self.photos[self.current_page_of_photos()])}"

    def display(self):
        dash_line = "-" * 11 + "\n"
        result = dash_line
        for page in self.photos:
            page_photos = ""
            for _ in page:
                page_photos += "[] "
            page_photos = page_photos.rstrip()
            result += (
                    page_photos + "\n"
                    + dash_line
            )

        return result


album = PhotoAlbum(2)
print(album.__dict__)
# album2 = PhotoAlbum.from_photos_count(9)
# print(album2.__dict__)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
# print(album.photos)
print(album.display())
