from array import array

from Color import Color


class PPM:
    width = 256
    height = 128
    max_val = 255
    new_Color = Color(0, 123, 1)

    # PPM Header
    ppm_header = f'P6 {width} {height} {max_val}\n'

    # PPM image data
    image = array.array('B', new_Color.__sizeof__() * width * height)

    # Save the PPM image as binary file
    with open('new_img.ppm', 'wb') as f:
        f.write(bytearray(ppm_header, 'ascii'))
        image.tofile(f)


