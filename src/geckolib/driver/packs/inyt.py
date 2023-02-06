#!/usr/bin/python3
"""
    GeckoPack - A class to manage the pack for 'InYT'
"""


class GeckoPack:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def name(self):
        return "InYT"

    @property
    def type(self):
        return 10

    @property
    def revision(self):
        return "36.01"
