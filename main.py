from threading import Thread

from doctors_page_handler import DoctorsPageHandler
from http_client import HttpClient
from helpers import Helpers
from queue_handler import QueueHandler

_SPECIALIZATION_NAME = "psycholog" # Specialization name
_NUM_THREADS = 5 # Number of threads
_START_PAGE = None # Start page (default: 1)
_END_PAGE = None # End page (default: end page of doctor search page)


def run_threads(queue, thread_worker):
    threads = []

    for _ in range(_NUM_THREADS):
        thread = Thread(target=thread_worker)
        thread.start()
        threads.append(thread)

    # Wait until all tasks are completed
    queue.join()

    # Wait for all threads to exit
    for thread in threads:
        thread.join()


def run():
    _http_client = HttpClient()
    _helpers = Helpers()
    _queue_handler = QueueHandler()
    
    _FIRST_PAGE = 1 if _START_PAGE is None else _START_PAGE
    _LAST_PAGE = _helpers.get_doctors_list_max_pages(
        _http_client.get_doctor_list_url(_SPECIALIZATION_NAME, 1)
    ) if _END_PAGE is None else _END_PAGE

    _queue_handler.fill_queue(_FIRST_PAGE, _LAST_PAGE + 1)
    _queue = _queue_handler.get_queue()

    def thread_worker():
        while True:
            try:
                # Raises queue.Empty if the queue is empty
                page = _queue.get_nowait()
            except Exception:
                break

            try:
                doctors_page_handler = DoctorsPageHandler(_SPECIALIZATION_NAME, page)
                doctors_page_handler.get_doctors_data()
            finally:
                _queue.task_done()

    run_threads(_queue, thread_worker)


if __name__ == "__main__":
    run()
