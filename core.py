import time

class PerformanceMonitor:
    def __init__(self):
        self.start_times = {}

    def start(self, task_name):
        self.start_times[task_name] = time.time()

    def stop(self, task_name):
        if task_name in self.start_times:
            elapsed_time = time.time() - self.start_times[task_name]
            print(f"{task_name} took {elapsed_time:.4f} seconds")
            del self.start_times[task_name]
        else:
            print(f"No record found for {task_name}")

# Example usage of PerformanceMonitor
if __name__ == '__main__':
    monitor = PerformanceMonitor()
    monitor.start('Task A')
    # Simulate some work with sleep
    time.sleep(2)
    monitor.stop('Task A')

    monitor.start('Task B')
    time.sleep(1.5)
    monitor.stop('Task B')