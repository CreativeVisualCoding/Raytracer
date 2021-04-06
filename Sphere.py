class Sphere:

    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    # checks if ray hits sphere. Returns distance to hit or None if there is no hit
    def intersects(self, ray):
        sphere_to_ray = ray.origin - self.center
        #a = 1
        b = 2 * ray.direction.dot_product(sphere_to_ray)
        c = sphere_to_ray.dot_product(sphere_to_ray) - self.radius * self.radius
        discriminant = b * b - 4 * c

