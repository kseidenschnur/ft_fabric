import threading
import queue

def worker(q):
    """Thread worker function"""
    print('Worker thread started')
    # do some work here...
    result = 42
    q.put(result)
    print('Worker thread finished')

# create a queue to communicate with the worker thread
q = queue.Queue()

# create a new thread
t = threading.Thread(target=worker, args=(q,))

# start the thread
t.start()

# main thread waits for result from worker thread
result = q.get()

# main thread continues execution
print(f'Result from worker thread: {result}')
print('Main thread finished')
