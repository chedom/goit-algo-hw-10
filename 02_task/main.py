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
    monte_carlo_n = [10, 100, 1000, 10000, 50000]
    monte_carlp_experiments = [1, 10, 50, 100]
    for n in monte_carlo_n:
        for experiment in monte_carlp_experiments:
            actual = find_integral_monte_carlo(quadratic, a, b, n, experiment)
            print(f"Actual: {actual}, N: {n}, experiments: {experiment}")

        print("-"*50)


if __name__ == "__main__":
    main()
