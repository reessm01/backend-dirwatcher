#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import dirwatcher
import subprocess
from helper.dir_search import dir_search
from helper.find_word import find_word


class TestStringMethods(unittest.TestCase):
    def test_dir_search_std(self):
        self.assertEqual(dir_search(".txt", "./watch_here"),
                         ['./watch_here/carl.txt', './watch_here/plain.txt'])

    def test_find_word(self):
        self.assertEqual(find_word(
            {"./watch_here/plain.txt": 0}, "hello"), {"./watch_here/plain.txt": 7})

    def test_help(self):
        process = subprocess.Popen(
            ["python", "./dirwatcher.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()
        self.assertEquals(stdout, usage)


if __name__ == '__main__':
    unittest.main()
