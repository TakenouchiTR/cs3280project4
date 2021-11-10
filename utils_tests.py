#!/usr/bin/env python3
"""
Tests for the utils.py lirary
"""
import unittest
import utils

__author__ = "Shawn Carter"
__version__ = "Fall 2021"
__pylint__ = "v1.8.3"

class TestScan(unittest.TestCase):
    """
    Tests for the scan() function
    """
    def test_single_open_port(self):
        """
        Tests if a single, open port is correctly detected
        """
        result = utils.scan("127.0.0.1", 10000)

        self.assertTrue(result[10000])
        
    def test_single_closed_port(self):
        """
        Tests if a single, closed port is correctly detected
        """
        result = utils.scan("127.0.0.1", 10003)

        self.assertFalse(result[10003])

    def test_many_open_ports(self):
        """
        Tests if many open ports are correctly detected
        """
        result = utils.scan("127.0.0.1", 10000, 10002)

        self.assertTrue(result[10000])
        self.assertTrue(result[10001])
        self.assertTrue(result[10002])
    
    def test_many_closed_ports(self):
        """
        Tests is many closed ports are correctly detected
        """
        result = utils.scan("127.0.0.1", 10003, 10005)

        self.assertFalse(result[10003])
        self.assertFalse(result[10004])
        self.assertFalse(result[10005])

    def test_many_open_and_closed_ports(self):
        """
        Tests if both open and closed ports are correctly detected
        """
        result = utils.scan("127.0.0.1", 10000, 10005)

        self.assertTrue(result[10000])
        self.assertTrue(result[10001])
        self.assertTrue(result[10002])
        self.assertFalse(result[10003])
        self.assertFalse(result[10004])
        self.assertFalse(result[10005])