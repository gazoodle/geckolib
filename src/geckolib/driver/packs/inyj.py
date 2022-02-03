#!/usr/bin/python3
"""
    GeckoPack - A class to manage the pack for 'InYJ'
"""


class GeckoPack:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def name(self):
        return "InYJ"

    @property
    def type(self):
        return 12

    @property
    def revision(self):
        return "33.00"
