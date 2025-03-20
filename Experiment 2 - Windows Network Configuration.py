import os 
import shutil 
 
# Windows hosts file location 
HOSTS_FILE = r"C:\Windows\System32\drivers\etc\hosts" 
 
def read_hosts(): 
    """Reads and displays the contents of the Windows hosts file.""" 
    if not os.path.exists(HOSTS_FILE): 
        print("[ERROR] Hosts file not found!") 
        return 
    try: 
        with open(HOSTS_FILE, 'r') as file: 
            print("\n===== Contents of hosts file =====\n") 
            print(file.read()) 
    except Exception as e: 
        print(f"[ERROR] Failed to read hosts file: {e}")

def modify_hosts(): 
    """Adds a custom hostname mapping to the Windows hosts file.""" 
    if not os.path.exists(HOSTS_FILE): 
        print("[ERROR] Hosts file not found!") 
        return 
    try: 
        # Backup the hosts file before modifying 
        shutil.copy(HOSTS_FILE, HOSTS_FILE + ".bak") 
        with open(HOSTS_FILE, "a") as file: 
            file.write("\n192.168.1.100 mycustomhost\n") 
        print("[SUCCESS] Hosts file updated.") 
    except Exception as e: 
        print(f"[ERROR] Failed to update hosts file: {e}")

def restart_network(): 
    """Flushes the DNS cache to apply changes.""" 
    try: 
        os.system("ipconfig /flushdns") 
        print("[SUCCESS] DNS cache flushed. Changes applied.") 
    except Exception as e: 
        print(f"[ERROR] Failed to flush DNS cache: {e}") 
 
if __name__ == "__main__": 
    # Step 1: Read and display the hosts file 
    #read_hosts() 
 
    # Step 2: Modify the hosts file 
    #modify_hosts() 
 
    # Step 3: Flush DNS cache to apply changes 
    restart_network()        
