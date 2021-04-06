from Image import Image
from Color import Color


def main():
    Width = 3
    Height = 2
    image = Image(Width, Height)
    red = Color(x=1, y=0, z=0)
    green = Color(x=0, y=1, z=0)
    blue = Color(x=0, y=0, z=1)

    image.set_pixel(0, 0, red)
    image.set_pixel(1, 0, green)
    image.set_pixel(2, 0, blue)

    image.set_pixel(0, 1, red + green)
    image.set_pixel(1, 1, red + blue + green)
    image.set_pixel(2, 1, red * 0.001)

    with open("test.ppm", "w") as img_file:
        image.write_ppm(img_file)


if __name__ == "__main__":
    main()
