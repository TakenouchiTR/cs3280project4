#!/usr/bin/env python3
"""
Utilities for project 4
Scans a range of ports to detect any open sockets.
"""
import multiprocessing
import socket

__author__ = "Shawn Carter"
__version__ = "Fall 2021"
__pylint__ = "v1.8.3"

def scan(ip_address, start_port, end_port = -1):
    """
    Scans a range of ports for the specified IP address, creating a dictionary containing
    key-value pairs for the scanned port and whether or not it's open. If end_port is not
    specified, only the start_port will be scanned.
    Args: ip_address - The target IP address to scan
          start_port - The start (inclusive) of the range of ports to scan
          end_port   - The end (inclusive) of the range of ports to scan
    Return: The list of links from the website
    """
    result = {}
    processes = []
    pipes = []

    if (end_port == -1):
        end_port = start_port

    for port in range(start_port, end_port + 1):
        pipe = multiprocessing.Pipe()
        process = multiprocessing.Process(target=check_socket, args=(ip_address, port, pipe[1]))

        processes.append(process)
        pipes.append(pipe[0])
        process.start()
    
    for process in processes:
        process.join()
    
    for pipe in pipes:
        message = pipe.recv()
        port, status = message.split(":")
        result[port] = status == "open"
    
    return result

def check_socket(ip_address, port, pipe):
    """
    Checks whether the target socket is open, then sends the result back through the provided pipe.
    Args: ip_address - The target IP address to scan
          port - The target port to scan
          pipe - The end of the pipe to return the result
    Return: None
    """
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if connection.connect_ex((ip_address, port)) == 0:
        pipe.send(f"{port}:open")
    else:
        pipe.send(f"{port}:closed")

if __name__ == '__main__':
    print(scan("127.0.0.1", 10000, 10000))