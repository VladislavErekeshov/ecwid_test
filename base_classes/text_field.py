from base_classes.base_еlement import BaseElement


class TextField(BaseElement):
    def __init__(self, locator, name):
        self.__locator = locator
        self.__name = name
        super().__init__(locator, name)


