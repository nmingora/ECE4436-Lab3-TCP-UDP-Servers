import socket
import time

# Configurations
HOST_ADDRESS = "127.0.0.1"
HOST_PORT = 12000
RECEIVE_BUFFER = 1024
DELAY_THRESHOLD = 1

def run_ping_test():
    # Initialize a UDP socket for the client
    ping_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Assign a timeout interval for the socket operations
    ping_socket.settimeout(DELAY_THRESHOLD)
    
    # Execute a series of pings to the server
    for ping_num in range(1, 11):
        # Construct the outgoing ping message
        ping_msg = f"Ping {ping_num} {time.strftime('%H:%M:%S')}"
        
        try:
            # Transmit the ping to the server endpoint
            ping_socket.sendto(ping_msg.encode(), (HOST_ADDRESS, HOST_PORT))
            
            # Note the send time
            send_time = time.time()
            
            # Await a reply from the server
            server_reply, _ = ping_socket.recvfrom(RECEIVE_BUFFER)
            
            # Calculate the elapsed time since sending the ping
            elapsed_time = time.time() - send_time
            
            # Display the server's reply and the elapsed time
            print(f"Reply from server: {server_reply.decode()}, Time elapsed: {elapsed_time:.2f}s")
        
        except socket.timeout:
            # Notify if no response received within the timeout period
            print("No response received within the set timeout period.")
    
    # Terminate the client socket after the pings
    ping_socket.close()

# This condition verifies if the script is the entry point to the program
if __name__ == "__main__":
    run_ping_test()


