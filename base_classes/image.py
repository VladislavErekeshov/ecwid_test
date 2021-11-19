from base_classes.base_еlement import BaseElement


class Image(BaseElement):
    def __init__(self, locator, name):
        super().__init__(locator, name)