import scipy.integrate as spi

from integral import find_integral_monte_carlo


def quadratic(x):
    return x**2


def main():
    a, b = 0, 2  # lower and upper boundary
    # calculate expected result
    expected_result, error = spi.quad(quadratic, a, b)
    print(f"Expected result: {expected_result}")
    # use Monte Carlo method
    monte_carlo_n = [100, 1000, 10000, 50000]
    for n in monte_carlo_n:
        actual = find_integral_monte_carlo(quadratic, a, b, n)
        print(f"Actual: {actual}, N: {n}")


if __name__ == "__main__":
    main()
