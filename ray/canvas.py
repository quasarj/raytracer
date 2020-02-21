from .color import Color

class Canvas:
    def __init__(self, width, height, color=Color(0, 0, 0)):
        self.width = width
        self.height = height

        self._length = width * height
        self._pixels = [color] * self._length

    def __iter__(self):
        self._iter_pos = 0
        self.__blank = Color(0, 0, 0)
        return self

    def __next__(self):
        if self._iter_pos < self._length:
            c = self._pixels[self._iter_pos]
            self._iter_pos += 1
            return c
        else:
            raise StopIteration

    def __getitem__(self, key):
        x, y = key
        pos = y * self.width + x
        return self._pixels[pos]

    def __setitem__(self, key, value):
        x, y = key
        pos = y * self.width + x
        self._pixels[pos] = value

    def gen_pixels(self):
        for pixel in self._pixels:
            yield str(pixel)

    def to_ppm(self):
        return f"""\
P3
{self.width} {self.height}
255
""" + '\n'.join(list(self.gen_pixels()))
