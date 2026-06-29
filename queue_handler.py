import queue


class QueueHandler:
    def __init__(self):
        self.queue = queue.Queue()

    def fill_queue(self, min: int, max: int) -> None:
        for i in range(min, max):
            self.queue.put(i)
