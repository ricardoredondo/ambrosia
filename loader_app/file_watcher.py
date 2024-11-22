import os
import time
import fnmatch
from main_loader import MainLoader
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Handler(FileSystemEventHandler):
    @staticmethod
    def on_created(event):
        if event.is_directory:
            return None
        else:
            print(f"Received created event - {event.src_path}")

    @staticmethod
    def on_modified(event):
        if event.is_directory:
            return None
        else:
            print(f"Received modified event - {event.src_path}")

class Watcher:
    def __init__(self, directory_to_watch, output_directory, interval):
        self.directory_to_watch = directory_to_watch
        self.output_directory = output_directory
        self.interval = interval
        self.observer = Observer()
        self.event_handler = FileSystemEventHandler()
        self.event_handler.on_created = self.on_created
  
    def on_created(self, event):
        print(f"New file created: {event.src_path}")
        self.go_to_load()

    def run(self):
        #  When service start will create a new version of the DB
        self.go_to_load()
        self.observer.schedule(self.event_handler, self.directory_to_watch, recursive=True)
        self.observer.start()
        
        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

    def go_to_load(self):
        print(f"Checking for Files...")
        files = self.list_files()

        if files:
            main_loader = MainLoader(files, 
                                    self.directory_to_watch, 
                                    self.output_directory)
            main_loader.run()
        else:
            print("No files to process.")

    def list_files(self):
        file_extensions = ['TXT', 'PDF']
        
        return [f for f in os.listdir(self.directory_to_watch) if os.path.isfile(os.path.join(self.directory_to_watch, f)) and any(fnmatch.fnmatch(f.lower(), f"*.{ext.lower()}") for ext in file_extensions)]