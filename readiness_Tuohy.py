print("Hello, I am Matthew Tuohy, and my student ID is 2178830")
def mean_and_max(numbers):
    mean = sum(numbers) / len(numbers)
    maximum = max(numbers)
    return mean, maximum
data = [1, 2, 3, 4, 5]
average, highest = mean_and_max(data)
print("list", data)
print("Mean", average)
print("Max", highest)
