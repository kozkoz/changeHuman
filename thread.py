from concurrent import futures
import time


def sample_func(index):
    print('index: %s started.' % index)
    sleep_seconds = random.randint(2, 4)
    time.sleep(sleep_seconds)
    print('index: %s ended.' % index)


future_list = []
with futures.ThreadPoolExecutor(max_workers=4) as executor:
    for i in range(20):
        future = executor.submit(fn=sample_func, index=i)
        future_list.append(future)
    _ = futures.as_completed(fs=future_list)

print('completed.')