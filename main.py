import array

from Color import Color

if __name__ == '__main__':
    width = 256
    height = 128
    max_val = 255
    new_Color = Color(0, 123, 1)

    # PPM Header
    ppm_header = f'P6 {width} {height} {max_val}\n'

    # PPM image data
    image = array.array('B', [0, 0, 255] * width * height)

  #  Fill with red the rectangle with origin at (10, 10) and width x height = 50 x 80 pixels

for y in range(10, 90):

    for x in range(10, 60) :
        index = 3 * (y * width + x)
        image[index] = 255  # red channel
        image[index + 1] = 0  # green channel
        image[index + 2] = 0  # blue channel


# Save the PPM image as binary file
    with open('new_img.ppm', 'wb') as f:
        f.write(bytearray(ppm_header, 'ascii'))
        image.tofile(f)
