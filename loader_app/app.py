import threading  
import time

from file_watcher import Watcher

if __name__ == '__main__':
    # Define constants
    OUTPUT_DIRECTORY    = "/storage_data"
    DIRECTORY_TO_WATCH  = "/source_loader"
    CHECK_INTERVAL      = 10                # Seconds


    print(f"============================================================")
    print("Starting Loader Service...")
    print(f"Source Folder: {DIRECTORY_TO_WATCH}")
    print(f"Storage Folder: {DIRECTORY_TO_WATCH}")
    print(f"============================================================")
    print(f"\n\n\n\n")

    w = Watcher(DIRECTORY_TO_WATCH, OUTPUT_DIRECTORY, CHECK_INTERVAL)
    
    # Start the file checker in a daemon thread
    daemon_thread = threading.Thread(target=w.run)
    daemon_thread.daemon = True
    daemon_thread.start()

    try:
        while True:
            time.sleep(1)  # Keep the main thread alive
    except KeyboardInterrupt:
        print("Stopping the file checker daemon.")