class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.queue = nums
        self.k = k

    def add(self, val: int) -> int:
        self.queue.append(val)
        return sorted(self.queue)[-self.k]
