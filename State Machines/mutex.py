import threading
import time

mutex = threading.Lock()
def get_data(cnt):
    mutex.acquire()
    try:
        thread_id = threading.get_ident()
        time.sleep(0.5)
        print(f"Count: {cnt} (thread {thread_id})")
    finally:
        mutex.release()

count = 1
max_count = 10
while True:
    thread = threading.Thread(target=get_data, args=(count,))
    thread.start()
    count = count + 1
    if count > max_count:
        break