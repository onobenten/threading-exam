import threading
import requests
import time

def get_data_sync(urls):
    st = time.time()
    json_array = []
    for url in urls:
        json_array.append(requests.get(url).json())
    et = time.time()
    elapsed_time = et - st
    print(f"Execution: {elapsed_time} seconds")
    return json_array

class ThreadingDownloader(threading.Thread):

    def __init__(self, url, result_list):
        super().__init__()
        self.url = url
        self.result_list = result_list

    def run(self):
        response = requests.get(self.url)
        self.result_list.append(response.json())

def get_data_threading(urls):
    st = time.time()
    threads = []
    json_array = []

    for url in urls:
        t = ThreadingDownloader(url, json_array)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    et = time.time()
    elapsed_time = et - st
    print(f"Execution: {elapsed_time} seconds")
    return json_array

urls = ["https://postman-echo.com/delay/3"] * 5
get_data_sync(urls)
data = get_data_threading(urls)
print(data)
