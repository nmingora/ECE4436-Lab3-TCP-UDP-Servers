import socket
import time

HOST_ADDRESS = "127.0.0.1"
HOST_PORT = 12000
RECEIVE_BUFFER = 1024
DELAY_THRESHOLD = 1

def run_ping_test():
    ping_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ping_socket.settimeout(DELAY_THRESHOLD)
    
    for ping_num in range(1, 11):
        ping_msg = f"Ping {ping_num} {time.strftime('%H:%M:%S')}"
        
        try:
            ping_socket.sendto(ping_msg.encode(), (HOST_ADDRESS, HOST_PORT))
            send_time = time.time()
            server_reply, _ = ping_socket.recvfrom(RECEIVE_BUFFER)
            elapsed_time = time.time() - send_time
            print(f"Reply from server: {server_reply.decode()}, Time elapsed: {elapsed_time:.2f}s")
        
        except socket.timeout:
            print("No response received within the set timeout period.")
    
    ping_socket.close()

if __name__ == "__main__":
    run_ping_test()
