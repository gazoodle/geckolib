#!/usr/bin/python3
"""
    GeckoPack - A class to manage the pack for 'MrSteam'
"""


class GeckoPack:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def name(self):
        return "MrSteam"

    @property
    def type(self):
        return 13

    @property
    def revision(self):
        return "33.00"
