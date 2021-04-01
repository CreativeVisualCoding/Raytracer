from Color import Color


class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[Color for _ in range(width)] for _ in range(height)]

    def set_pixel(self, x, y, color):
        self.pixels[y][x] = color

    def write_ppm(self, img_file):
        def to_byte(c):
            return round(max(min(c * 255), 0))

        for row in self.pixels:
            for new_color in row:
                img_file.write("{} {} {} ".format(
                    to_byte(new_color.getRed()),
                    to_byte(new_color.getGreen()),
                    to_byte(new_color.getBlue())
                )
                )
