import time
import threading
from queue import Queue
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher:
    DIRECTORY_TO_WATCH = "/storage_data"

    def __init__(self):
        self.observer = Observer()
        self.event_queue = Queue()

    def run(self):
        event_handler = Handler(self.event_queue)
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()

        worker_thread = threading.Thread(target=self.process_events)
        worker_thread.start()

        try:
            while True:
                print("Waiting for 20s")
                time.sleep(20)
        except KeyboardInterrupt:
            self.observer.stop()
            self.event_queue.put(None)  # Signal the worker thread to exit
            worker_thread.join()
        self.observer.join()

    def process_events(self):
        while True:
            event = self.event_queue.get()
            if event is None:
                break  # Exit the loop if None is received
            print(f"Processing event: {event}")

class Handler(FileSystemEventHandler):
    def __init__(self, event_queue):
        self.event_queue = event_queue

    def on_created(self, event):
        if not event.is_directory:
            self.event_queue.put({
                'event_type': 'created',
                'src_path': event.src_path
            })

    def on_modified(self, event):
        if not event.is_directory:
            self.event_queue.put({
                'event_type': 'modified',
                'src_path': event.src_path
            })

if __name__ == '__main__':
    w = Watcher()
    w.run()