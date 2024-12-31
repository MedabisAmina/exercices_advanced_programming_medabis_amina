def length(lst):
    """
    Returns the number of elements in the list.
    Args:
        lst (list): The input list.
    Returns:
        int: Number of elements in the list.
    """
    return len(lst)

def mean(lst):
    """
    Calculates the arithmetic mean of the list.
    Args:
        lst (list): The input list.
    Returns:
        float: The mean of the list elements, or None if the list is empty.
    """
    if not lst:
        return None
    return sum(lst) / len(lst)

def range_of_list(lst):
    """
    Returns the difference between the maximum and minimum values in the list.
    Args:
        lst (list): The input list.
    Returns:
        float: The range of the list, or None if the list is empty.
    """
    if not lst:
        return None
    return max(lst) - min(lst)

def median(lst):
    """
    Calculates the median of the list.
    Args:
        lst (list): The input list.
    Returns:
        float: The median of the list, or None if the list is empty.
    """
    if not lst:
        return None
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

def standard_deviation(lst):
    """
    Calculates the standard deviation of the list.
    Args:
        lst (list): The input list.
    Returns:
        float: The standard deviation, or None if the list has fewer than 2 elements.
    """
    if len(lst) < 2:
        return None
    m = mean(lst)
    variance = sum((x - m) ** 2 for x in lst) / len(lst)
    return variance ** 0.5

def list_statistics(lst):
    """
    Creates a dictionary with statistics about the list.
    Args:
        lst (list): The input list.
    Returns:
        dict: A dictionary with length, mean, range, median, and standard deviation.
    """
    if not isinstance(lst, list):
        return "Input must be a list."
    if any(not isinstance(x, (int, float)) for x in lst):
        return "List must contain only numeric values."

    return {
        "length": length(lst),
        "mean": mean(lst),
        "range": range_of_list(lst),
        "median": median(lst),
        "standard_deviation": standard_deviation(lst)
    }

# Test cases
if __name__ == "__main__":
    test_cases = [
        [],
        [5],
        [-10, -5, 0, 5, 10],
        [1.5, 2.5, 3.5, 4.5, 5.5],
        [1, 2, 3, 4, 5]
    ]

    for test_case in test_cases:
        print(f"Input: {test_case}")
        print(f"Statistics: {list_statistics(test_case)}")
        print()
