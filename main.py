from Color import Color
from Image import Image


def main():
    Width = 3
    Height = 2
    image = Image(Width, Height)
    red = Color(1, 0, 0)
    green = Color(0, 1, 0)
    blue = Color(0, 0, 1)

    image.set_pixel(0, 1, red + blue)
    image.set_pixel(1, 1, red + blue + green)
    image.set_pixel(2, 1, red*0.001)

    with open("test.ppm", "w") as img_file:
        image.write_ppm(img_file)


if __name__ == "__main__":
    main()
