#!/usr/bin/env python3
"""
Tests for the utils.py library.
Ports 50000-50002 must be opened for tests to pass.
"""
import unittest
import multiprocessing
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
        result = utils.scan("127.0.0.1", 50000)

        self.assertTrue(result[50000])

    def test_single_closed_port(self):
        """
        Tests if a single, closed port is correctly detected
        """
        result = utils.scan("127.0.0.1", 50003)

        self.assertFalse(result[50003])

    def test_many_open_ports(self):
        """
        Tests if many open ports are correctly detected
        """
        result = utils.scan("127.0.0.1", 50000, 50002)

        self.assertTrue(result[50000])
        self.assertTrue(result[50001])
        self.assertTrue(result[50002])

    def test_many_closed_ports(self):
        """
        Tests is many closed ports are correctly detected
        """
        result = utils.scan("127.0.0.1", 50003, 50005)

        self.assertFalse(result[50003])
        self.assertFalse(result[50004])
        self.assertFalse(result[50005])

    def test_many_open_and_closed_ports(self):
        """
        Tests if both open and closed ports are correctly detected
        """
        result = utils.scan("127.0.0.1", 50000, 50005)

        self.assertTrue(result[50000])
        self.assertTrue(result[50001])
        self.assertTrue(result[50002])
        self.assertFalse(result[50003])
        self.assertFalse(result[50004])
        self.assertFalse(result[50005])

class TestCheckSocket(unittest.TestCase):
    """
    Tests for the check_socket() function
    """
    def test_socket_open(self):
        """
        Tests if an open socket is properly detected
        """
        pipe = multiprocessing.Pipe()

        utils.check_socket("127.0.0.1", 50000, pipe[1])
        result = pipe[0].recv()

        self.assertEqual("50000:open", result)

    def test_socket_closed(self):
        """
        Tests if an closed socket is properly detected
        """
        pipe = multiprocessing.Pipe()

        utils.check_socket("127.0.0.1", 50003, pipe[1])
        result = pipe[0].recv()

        self.assertEqual("50003:closed", result)
