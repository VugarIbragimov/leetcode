from typing import Any, List

nums = [1, 2, 3]
targ = 4


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(numbers):
            remaining = target - numbers[i]
            if remaining in seen:
                return [seen[remaining]+1, i+1]
            else:
                seen[value] = i


test = Solution.twoSum(Solution, numbers=nums, target=targ)
print(test)

a = -27 // 4
print(a)





import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения {func.__name__}: {execution_time:.4f} секунд")
        return result
    return wrapper



import time

def retry(max_attempts, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed: {e}")
                    time.sleep(delay)
            print(f"Function failed after {max_attempts} attempts")
        return wrapper
    return decorator


class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = time.time() - self.start_time
        print(f"Elapsed time: {elapsed_time} seconds")


class Singleton(object):
    _instance = None

    def __new__(cls_, *args, **kwargs):
        if not isinstance(cls_._instance, cls_):
            cls_._instance = object.__new__(cls_, *args, **kwargs)
        return cls_._instance


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]