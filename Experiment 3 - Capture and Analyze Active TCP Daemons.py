import psutil 
 
def list_tcp_connections(): 
    for conn in psutil.net_connections(kind='tcp'): 
        print(f"PID: {conn.pid}, Local Address: {conn.laddr}, Remote Address: {conn.raddr}, Status: {conn.status}") 
 
list_tcp_connections() 
