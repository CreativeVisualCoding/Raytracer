from Image import Image
from Color import Color
from Point import Point
from Vector import Vector


def main():
    Width = 320
    Height = 200
    camera = Vector(0, 0, -1)
    objects = [Sphere(Point(0, 0, 0,), 0.5, Color.from_hex("#FF0000"))]
    scene = Scene(camera, objects, Width, Height)
    engine = RenderEnginge()
    image = engine.render(scene)

    with open("test.ppm", "w") as img_file:
        image.write_ppm(img_file)


if __name__ == "__main__":
    main()
