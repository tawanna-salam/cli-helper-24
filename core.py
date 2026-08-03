import time

class PerformanceOptimizer:
    def __init__(self):
        self.execution_times = []

    def time_function(self, func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            self.execution_times.append(end_time - start_time)
            return result
        return wrapper

    def average_execution_time(self):
        if not self.execution_times:
            return 0
        return sum(self.execution_times) / len(self.execution_times)

@PerformanceOptimizer().time_function
def compute_heavy_task(x):
    # Simulate a heavy computational task
    total = 0
    for i in range(1, x + 1):
        total += i ** 2
    return total

if __name__ == '__main__':
    print(compute_heavy_task(10000))
    print('Average execution time:', PerformanceOptimizer().average_execution_time())