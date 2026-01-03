import random


def find_integral_monte_carlo(fn, a, b, n):
    # find the average value of the func on a span [a, b]
    sum = 0

    for _ in range(n):
        x = random.uniform(a, b)  # get a random `x` in [a, b]
        y = fn(x)  # calculate `y` for a randon `x`
        sum += y

    average_y = sum / n

    # the value of integral is an area of a rectancle with
    # with width: `b - a` and heigth: `average_y`
    return (b-a) * average_y
