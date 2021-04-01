from Image import Image
from Color import Color


def main():
    Width = 3
    Height = 2
    image = Image(Width, Height)
    red = Color(1, 0, 0)
    green = Color(0, 1, 0)
    blue = Color(0, 0, 1)

    old_red = red

    image.set_pixel(0, 1, red.add_color(green))
    image.set_pixel(1, 1, red.add_color(blue))
    image.set_pixel(2, 1, old_red.multiply_float(0.001))

    with open("test.ppm", "w") as img_file:
        image.write_ppm(img_file)


if __name__ == "__main__":
    main()
