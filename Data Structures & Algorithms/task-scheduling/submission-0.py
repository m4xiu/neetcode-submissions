from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_frequency = max(task_counts.values())
        num_max_frequency_tasks = sum(1 for count in task_counts.values() if count == max_frequency)
        min_time = max(len(tasks), (max_frequency - 1) * (n + 1) + num_max_frequency_tasks)
      
        return min_time
