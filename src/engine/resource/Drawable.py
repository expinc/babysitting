class Drawable:
    def __init__(self, surface = None):
        self.surface = surface


    def size(self):
        return self.surface.get_size()


class Image(Drawable):
    def __init__(self, surface = None):
        super().__init__(surface)


class Text(Drawable):
    def __init__(self, surface = None):
        super().__init__(surface)