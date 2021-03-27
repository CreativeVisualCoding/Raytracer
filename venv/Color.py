green_warning = '\033[92m'
blue_warning = '\033[94m'
red_warning = '\033[93m'
ENDC = '\033[0m'


class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def add_color(self, color_new):
        if self.red < 0:
            self.red = 0
            print('\t' + red_warning + "Error in red part of Color" + ENDC + '\n')
        if self.green < 0:
            self.green = 0
            print('\t' + green_warning + "Error in green part of Color" + ENDC+'\n')
        if self.blue < 0:
            self.blue = 0
            print('\t' + blue_warning + "Error in blue part of Color" + ENDC + '\n')
        self.red += Color_New.red
        self.green += Color_New.green
        self.blue += Color_New.blue
        if self.red > 1:
            self.red = 1
        if self.green > 1:
            self.green = 1
        if self.blue > 1:
            self.blue = 1

    def subtract_color(self, color_new):
        self.red -= Color_New.red
        self.green -= Color_New.green
        self.blue -= Color_New.blue
        if self.red < 0:
            self.red = 0
        if self.green < 0:
            self.green = 0
        if self.blue < 0:
            self.blue = 0

    def print_color(self):
        print(f"Color :{self.red, self.green, self.blue}")
