import math

def read_file(filename="log.txt"):  # Reading the text file and collecting the numbers in the form of list
    try:
        with open(filename, 'r') as file:
            line = file.readline().strip()
            if not line:
                return []
            return [float(num) for num in line.split()]
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{filename}' was not found")
    except ValueError:
        raise ValueError("The file contains non-numeric values")

def _standard_deviation(data): # Standard deviation fn
    if len(data) < 2:
        raise ValueError("Standard deviation requires at least 2 data points")
    mean = sum(data) / len(data)
    squared_diffs = [(x - mean) ** 2 for x in data]
    variance = sum(squared_diffs) / (len(data) - 1)
    return math.sqrt(variance)

def _median(data): # Median fn
    if not data:
        raise ValueError("Cannot calculate median of an empty list")
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 1:
        return sorted_data[mid]
    return (sorted_data[mid - 1] + sorted_data[mid]) / 2

def muchiko_filter(data, window_size): # Muchiko fileter logic
    if len(data) < window_size:
        raise ValueError("Window size must be ≤ data length")
    if window_size <= 0:
        raise ValueError("Window size must be positive")
    return [sum(data[i:i + window_size]) / window_size for i in range(len(data) - window_size + 1)]

def sanchiko_filter(data, window_size): # Sanchiko fn logic
    if len(data) < window_size:
        raise ValueError("Window size must be ≤ data length")
    if window_size <= 0:
        raise ValueError("Window size must be positive")
    return [_median(data[i:i + window_size]) for i in range(len(data) - window_size + 1)]

data = read_file()
if not data:
    print("File is empty")
else: # Checking for the best method for noice reduction
    window_size = (len(data) // 2) + 1
    mean_filtered = muchiko_filter(data, window_size)
    median_filtered = sanchiko_filter(data, window_size)
    std_mean = _standard_deviation(mean_filtered)
    std_median = _standard_deviation(median_filtered)

    if std_mean > std_median:
        print("Median filtered data:", median_filtered)
        print("Noise Removed" if std_median == 0 else "Smoothed data")
    else:
        print("Mean filtered data:", mean_filtered)
        print("Noise Removed" if std_mean == 0 else "Smoothed data")