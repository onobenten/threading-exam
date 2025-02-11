import threading
import requests
import time 
import asyncio
import aiohttp

#asyncio internetle çalışırken kullanılır Coroutines yapısı aklımıza gelsin
# Coroutines yapısı sunucularla çalışırken tercih edilebilir birden fazla istek gidince bu yöntem isteklerin kordine edilmesinde daha verimli olablir.
#android geliştirmede de kullanılır
#async ve await kelimeleri aklımıza gelsin
#geather fonksiyonu ile birden fazla coroutine oluşturulabilir bunu yapmak için de ensure_future kullanmak gerekir 


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
    json_array = []

    def __init__(self,url):
        super().__init__()
        self.url = url

    def run(self):
        response = requests.get(self.url)
        self.json_array.append(response.json())
        print(self.json_array)
        return super().run()
def get_data_threading(urls):
    st = time.time()
    threads = []
    for url in urls:
        t = ThreadingDownloader(url)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
        print(t)   

    et = time.time()
    elapsed_time = et - st
    print(f"Execution: {elapsed_time} seconds")
   
async def get_data_async_but_as_wrapper(urls):
        st = time.time()
        json_array = []

        async with aiohttp.ClientSession() as session:
            for url in urls:
                async with session.get(url) as resp:
                    json_array.append(await resp.json())


        et = time.time()
        elapsed_time = et - st
        print("execution time: " ,elapsed_time, "seconds")
        return json_array


async def get_data(session,url, json_array):
    async with session.get(url) as resp:
        json_array.append(await resp.json())

async def get_data_async_concurrently(urls):
    st = time.time()
    json_array = []

    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(asyncio.ensure_future(get_data(session,url,json_array)))
        await asyncio.gather(*tasks)

    et = time.time()
    elapsed_time = et - st
    print("execution time: " ,elapsed_time, "seconds")
    return json_array


urls = ["https://postman-echo.com/delay/3"] * 5
#get_data_sync(urls) #18.4
#asyncio.run(get_data_async_but_as_wrapper(urls))
asyncio.run(get_data_async_concurrently(urls))