#stats


def compute_mean(ratings):
    if not ratings:
        raise ValueError("compute_stats: ratings list is empty")
    total = sum(ratings)
    count = len(ratings)
    return total / count

def compute_min(ratings):
    if not ratings:
        raise ValueError("compute_stats: ratings list is empty")
    minimum = ratings[0]
    for value_min in ratings:
        if value_min < minimum:
            minimum = value_min
    return minimum

def compute_min_fast(ratings):
    if not ratings:
        raise ValueError("compute_stats: ratings list is empty")
    return min(ratings)

def compute_max(ratings):
    if not ratings:
        raise ValueError("compute_stats: ratings list is empty")
    maximum = ratings[0]
    for value in ratings:
        if value > maximum:
            maximum = value
    return maximum

def compute_max_fast(ratings):
    if not ratings:
        raise ValueError("compute_stats: ratings list is empty")
    return max(ratings)

def compute_stats(ratings):
    if not ratings:
        raise ValueError("compute_stats: ratings list is empty")
    return {
        "mean": compute_mean(ratings),
        "min": compute_min_fast(ratings),
        "max": compute_max_fast(ratings),
        "count": len(ratings)
    }

