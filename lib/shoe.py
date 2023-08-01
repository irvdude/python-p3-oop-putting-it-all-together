#!/usr/bin/env python3


class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self._condition = "Used"

    def get_size(self):
        return self._size

    def set_size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")

    size = property(
        get_size,
        set_size,
    )

    def get_brand(self):
        return self._brand

    def set_brand(self, brand):
        self._brand = brand

    brand = property(
        get_brand,
        set_brand,
    )

    def cobble(self):
        print("Your shoe is as good as new!")
        self._condition = "New"

    @property
    def condition(self):
        return self._condition
