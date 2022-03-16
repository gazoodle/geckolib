#!/usr/bin/python3
"""
    GeckoPack - A class to manage the pack for 'MAS-IBC-16K'
"""


class GeckoPack:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def name(self):
        return "MAS-IBC-16K"

    @property
    def type(self):
        return 2

    @property
    def revision(self):
        return "33.00"
