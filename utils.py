import multiprocessing
import socket

def scan(ip_address, start_port, end_port):
    result = {}
    processes = []
    pipes = []

    for port in range(start_port, end_port + 1):
        pipe = multiprocessing.Pipe()
        process = multiprocessing.Process(target=scan_socket, args=(ip_address, port, pipe[1]))

        processes.append(process)
        pipes.append(pipe[0])
        process.start()
    
    for process in processes:
        process.join()
    
    for pipe in pipes:
        message = pipe.recv()
        parts = message.split(":")
        result[parts[0]] = parts[1] == "open"
    
    return result

def scan_socket(ip_address, port, pipe):
    try:
        connection = socket.create_connection((ip_address, port))
        pipe.send(f"{port}:open")
    except:
        pipe.send(f"{port}:closed")
    

if __name__ == '__main__':
    print(scan("127.0.0.1", 10000, 10000))