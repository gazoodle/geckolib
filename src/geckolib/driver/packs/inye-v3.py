#!/usr/bin/python3
"""
    GeckoPack - A class to manage the pack for 'inYE-V3'
"""


class GeckoPack:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def name(self):
        return "inYE-V3"

    @property
    def type(self):
        return 10

    @property
    def revision(self):
        return "36.01"
