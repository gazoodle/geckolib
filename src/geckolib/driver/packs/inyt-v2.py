#!/usr/bin/python3
"""
    GeckoPack - A class to manage the pack for 'InYT-V2'
"""


class GeckoPack:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def name(self):
        return "InYT-V2"

    @property
    def type(self):
        return 10

    @property
    def revision(self):
        return "33.00"
