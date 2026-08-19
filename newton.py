def f_x(x):
    return x**3 + (2 * x**2) + 1


def derivative(func, x, epsilon=0.001):
    if callable(func):
        return (func(x + epsilon) - func(x)) / epsilon
    else:
        return 0


def derivative_second(func, x, epsilon=0.001):
    if callable(func):
        return (
            derivative(func, x + epsilon, epsilon) - derivative(func, x, epsilon)
        ) / epsilon
    else:
        return 0


def newtons_method(func, x, epsilon=0.001):
    """
    Parameters:
        f_x - the function you want to optimize
        x_init - the intial x0 value
        epsilon - the error difference before accepting the value as the optimized output
    Returns the value that optimizes a binomial
    """

    curr_val = x
    next_val = float("-inf")
    difference = float("inf")
    # while the difference is large
    while difference > epsilon:
        first_derivative = derivative(func, curr_val, epsilon)
        second_derivative = derivative_second(func, curr_val, epsilon)

        next_val = curr_val - (first_derivative / second_derivative)
        difference = abs(next_val - curr_val)
        curr_val = next_val
        next_val = float("-inf")

    return {'new x': curr_val, 'value': func(curr_val)}
