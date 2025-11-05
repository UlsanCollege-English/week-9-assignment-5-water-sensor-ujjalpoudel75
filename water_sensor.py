import heapq

def streaming_median(nums):
    if not nums:
        return []

    low = []   # max-heap (store negatives)
    high = []  # min-heap
    result = []

    for num in nums:
        # Step 1: Insert into one of the heaps
        if not low or num <= -low[0]:
            heapq.heappush(low, -num)
        else:
            heapq.heappush(high, num)

        # Step 2: Balance heaps so that len(low) >= len(high) and diff <= 1
        if len(low) > len(high) + 1:
            heapq.heappush(high, -heapq.heappop(low))
        elif len(high) > len(low):
            heapq.heappush(low, -heapq.heappop(high))

        # Step 3: Compute median
        if len(low) == len(high):
            median = (-low[0] + high[0]) / 2.0
        else:
            median = -low[0]

        result.append(median)

    return result
