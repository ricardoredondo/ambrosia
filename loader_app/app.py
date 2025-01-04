import threading  
import time
from file_watcher import Watcher

if __name__ == '__main__':
    # This is the main entry point for the Loader Service. From this location
    # we will load the PDF files. THen we  split the content into smaller 
    # chunks and store them as vectors in the Vector DB
    DIRECTORY_TO_WATCH  = "/source_loader"
    
    # The is the location where the Vector DB will store the data
    OUTPUT_DIRECTORY    = "/storage_data"
    
    print(f"============================================================")
    print("Starting Loader Service...")
    print(f"Source Folder: {DIRECTORY_TO_WATCH}")
    print(f"Storage Folder: {OUTPUT_DIRECTORY}")
    print(f"============================================================")
    print(f"\n\n\n\n")

    w = Watcher(DIRECTORY_TO_WATCH, OUTPUT_DIRECTORY)
    
    # Starts the Deamon Thread
    daemon_thread = threading.Thread(target=w.run)
    daemon_thread.daemon = True
    daemon_thread.start()

    
    # Keep the main thread alive
    # By keeping the main process alive, all threads will remain alive. 
    # We can stop the daemon thread by pressing Ctrl+C
    try:
        while True:
            time.sleep(1)                   
    except KeyboardInterrupt:
        print("Stopping the file checker daemon.")