from multiprocessing import Process, Queue
from memory_profiler import memory_usage
from typing import Callable, Optional


def _function_max_memory_usage_children(f: Callable, queue: Queue, args=None) -> Optional[float]:
    queue.put(
        memory_usage((f, args), interval=.001, max_usage=True))


def function_max_memory_usage(f: Callable, args) -> float:
    q = Queue()
    p = Process(target=_function_max_memory_usage_children, args=(f, q, args))
    p.start()
    p.join()
    return q.get()
