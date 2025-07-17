import math

def standard_deviation(data):
    mean = sum(data) / len(data)  # calculate the mean
    # calculate the squared differences for each element in data
    square_difference = [(score - mean) ** 2 for score in data]
    
    variance = sum(square_difference) / len(data)  # calculate variance
    std_deviation = math.sqrt(variance)  # calculate standard deviation
    
    return mean, variance, std_deviation  # return mean, variance, and standard deviation

data = [10, 20, 10, 5, 15]

mean, variance, std_deviation = standard_deviation(data)

print(f"Mean: {mean}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_deviation}")
