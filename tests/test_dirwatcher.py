#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import dirwatcher
import subprocess

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        # self.assertEqual(dirwatcher.to_upper("foo"), "FOO")
        # example test for reference
        pass

    def test_all_options(self):
        # process = subprocess.Popen(
        #     ["../", ".jpg", "whats up dude", "-utl"],
        #     stdout=subprocess.PIPE)
        # stdout, _ = process.communicate()

        # self.assertEqual(stdout, "Whats Up Dude\n")
        pass

    def test_help(self):
        process = subprocess.Popen(
            ["python", "./dirwatcher.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()
        print(usage)
        self.assertEquals(stdout, usage)

if __name__ == '__main__':
    dirwatcher.main()