""" Tests of source/ground.py """
import os
import unittest

import source.ground as grd

if __name__ == "__main__":
    os.chdir("..")


class Test_this_module(unittest.TestCase):
    def test_origin_module(self):
        origin_module_name = grd.get_calling_module(0)
        self.assertEqual('ground', origin_module_name)

    def test_this_module(self):
        this_module_name = grd.get_calling_module(1)
        self.assertEqual(__name__, this_module_name)


