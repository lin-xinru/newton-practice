def f_x(x):
    return x^3

def derivative_f_x(x):
    return 3*(x^2)

def newtons_method(x_init, func):
    curr_val = x_init
    next_val = x_init
    difference = 0
    epsilon = 0.1 #not sure what this should be
    # while the difference is small
    # while (difference > epsilon) :
        # first_derivative = diff.derivative(func)
        # second_derivative = diff.derivative(first_derivative)

        # next_val = curr_val - (first_derivative(curr_val)/second_derivative(curr_val))
        # difference = math.abs(next_val-curr_val)
        # curr_val = next_val


if __name__ == '__main__':
    x = Symbol('x')
    derivative(x^2)