#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import dirwatcher
import subprocess
from helper.dir_search import dir_search

class TestStringMethods(unittest.TestCase):
    def test_dir_search_std(self):
        self.assertEqual(dir_search(".txt", "./watch_here"), ['carl.txt', 'plain.txt'])

    def test_help(self):
        process = subprocess.Popen(
            ["python", "./dirwatcher.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()
        self.assertEquals(stdout, usage)

if __name__ == '__main__':
    unittest.main()