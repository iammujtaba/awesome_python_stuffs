import threading
import queue

class MessageProcessor:
    def __init__(self, num_workers=1):
        self.num_workers = num_workers
        self.message_queue = queue.Queue()
        self.workers = []

    def process_message(self, message):
        print("processing message:", message)

    def worker(self):
        while True:
            message = self.message_queue.get()
            if message is None:
                break
            self.process_message(message)
            self.message_queue.task_done()

    def start(self):

        for _ in range(self.num_workers):
            worker_thread = threading.Thread(target=self.worker)
            worker_thread.start()
            self.workers.append(worker_thread)

    def stop(self):
        for _ in range(self.num_workers):
            self.message_queue.put(None)
        for worker_thread in self.workers:
            worker_thread.join()

    def enqueue_message(self, message):
        self.message_queue.put(message)



message_processor = MessageProcessor(num_workers=4)


message_processor.start()

for i in range(10):
    message_processor.enqueue_message(f"Message {i}")


message_processor.stop()
