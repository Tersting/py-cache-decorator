from typing import Callable, Any


def cache(func: Callable) -> Callable:
    memory_dict = {}

    def inner(*args, **kwargs) -> Any:
        key = (*args, tuple(sorted(kwargs.items())))

        if key in memory_dict:
            print("Getting from cache")
            return memory_dict[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            memory_dict[key] = result
            return result

    return inner
