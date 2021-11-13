#!/usr/bin/env python3
"""
Script for checking whether ports are open or closed.
"""
import sys
import utils

__author__ = "Shawn Carter"
__version__ = "Fall 2021"
__pylint__ = "v1.8.3"

def main():
    """
    The main entry point for the script
    """
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Incorrect parameters. Please use <IP address> <Starting port> [Ending port]")
        sys.exit(1)

    if len(sys.argv) == 3:
        print(utils.scan(sys.argv[1], int(sys.argv[2])))
    else:
        print(utils.scan(sys.argv[1], int(sys.argv[2]), int(sys.argv[3])))

if __name__ == "__main__":
    main()
